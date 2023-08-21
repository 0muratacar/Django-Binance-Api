from django.conf import settings
from django.shortcuts import render
from binance.client import Client
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError, JsonResponse
from app.tasks import add
from env_config import api_key, api_secret
import logging
from .models import Balance
from .serializers import BalanceSerializer
from rest_framework.decorators import api_view


def index(request):
    if request.method == 'GET':
        if (not (hasattr(settings, 'BINANCE_CLIENT'))):
            error_message = "Check Binance Client!"
            return JsonResponse({"error": error_message}, status=500)

        getItFromDebug1 = 'hellloo'
        getItFromDebug2 = 'Hi'
        add.delay(2, 3)
        # DEBUG
        # import pdb;pdb.set_trace()
        return JsonResponse({"message": "Binance initilaized succesfully!"}, status=200)


def getAccount(request):
    if request.method == 'GET':
        if (not (hasattr(settings, 'BINANCE_CLIENT'))):
            error_message = "Check Binance Client!"
            return JsonResponse({"error": error_message}, status=500)
        account = settings.BINANCE_CLIENT.get_account()
        return JsonResponse({"message": account}, status=200)


def BalancesApi(request):
    if request.method == 'GET':
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


@api_view(['GET', 'POST'])
def BalancesDb(request, id):
    if request.method == 'GET':
        if id is not None:
            try:
                balance = Balance.objects.get(id=id)
                serializer = BalanceSerializer(balance)
                return JsonResponse(serializer.data, status=200)
            except Balance.DoesNotExist:
                return JsonResponse({"message": "Balance not found"}, status=404)

    elif request.method == 'POST':
        serializer = BalanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
