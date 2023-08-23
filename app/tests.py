
from django.test import TestCase, RequestFactory
from unittest.mock import MagicMock, patch
from app.models import Balance
from app.views import BalancesDb, index, getAccount, BalancesApi


class ViewTests(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_index_view(self):
        request = self.factory.get('/')
        response = index.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Binance initilaized succesfully!', response.content)

    def test_getAccount_view(self):
        with patch('django.conf.settings.BINANCE_CLIENT') as mock_binance_client:
            mock_binance_client.get_account.return_value = {'balances': []}
            request = self.factory.get('/account')
            response = getAccount.as_view()(request)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'"balances": []', response.content)

    def test_BalancesApi_view(self):
        with patch('django.conf.settings.BINANCE_CLIENT') as mock_binance_client:
            mock_binance_client.get_account.return_value = {
                'balances': [{'free': '2'}]}
            request = self.factory.get('/balances-api')
            response = BalancesApi.as_view()(request)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'"message": [{"free": "2"}]', response.content)

    def test_BalancesDb_view_success(self):
        balance = Balance.objects.create(name="TestBalance", balance=100.0)
        request = self.factory.get('/balances-db/1')
        response = BalancesDb.as_view()(request, id=balance.id)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'"balance": 100.0', response.content)

    def test_BalancesDb_view_error(self):
        request = self.factory.get('/balances-db/999')  
        response = BalancesDb.as_view()(request, id=999)
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'"message": "Balance not found!"', response.content)