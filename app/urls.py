from django.urls import path

from . import views

urlpatterns = [
    path("", views.index.as_view(), name="index"),
    path("account", views.getAccount.as_view(), name="getAccount"),
    path("balances-api", views.BalancesApi.as_view(), name="getBalancesFromApi"),
    path("balances-db", views.BalancesDb.as_view(), name="getBalancesFromDb"),
    path("balances-db/<int:id>", views.BalancesDb.as_view(), name="getBalanceFromDb"),
]
