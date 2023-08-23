from django.conf import settings
from django.shortcuts import get_object_or_404, render
from binance.client import Client
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError, JsonResponse
from app.tasks import add
from env_config import api_key, api_secret
import logging
from .models import Balance
from .serializers import BalanceSerializer
from rest_framework.decorators import api_view
from django.views import View


class index(View):
    def get(self, request):
        if (not (hasattr(settings, 'BINANCE_CLIENT'))):
            error_message = "Check Binance Client!"
            return JsonResponse({"error": error_message}, status=500)

        getItFromDebug1 = 'hellloo'
        getItFromDebug2 = 'Hi'
        add.delay(2, 3)
        # DEBUG
        # import pdb;pdb.set_trace()
        return JsonResponse({"message": "Binance initilaized succesfully!"}, status=200)


class getAccount(View):
    def get(self, request):
        if (not (hasattr(settings, 'BINANCE_CLIENT'))):
            error_message = "Check Binance Client!"
            return JsonResponse({"error": error_message}, status=500)
        account = settings.BINANCE_CLIENT.get_account()
        return JsonResponse({"message": account}, status=200)


class BalancesApi(View):
    def get(self, request):
        if (not (hasattr(settings, 'BINANCE_CLIENT'))):
            error_message = "Check Binance Client!"
            return JsonResponse({"error": error_message}, status=500)
        account = settings.BINANCE_CLIENT.get_account()
        balances = account['balances']
        assets = []
        for balance in balances:
            if float(balance['free']) > 0:
                assets.append(balance)
        return JsonResponse({"message": assets}, status=200)


class BalancesDb(View):
    def get(self, request, id=None, *args, **kwargs):
        if id is None:
            balances = Balance.objects.all()
            serializer = BalanceSerializer(balances, many=True)
            return JsonResponse(serializer.data, status=200, safe=False)
        else:
            try:
                balance = Balance.objects.get(id=id)
                serializer = BalanceSerializer(balance)
                return JsonResponse(serializer.data, status=200)
            except Balance.DoesNotExist:
                return JsonResponse({"message": "Balance not found!"}, status=404)
