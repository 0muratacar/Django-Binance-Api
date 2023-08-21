from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("account", views.getAccount, name="getAccount"),
    path("balances-api", views.BalancesApi, name="getBalancesFromApi"),
    path("balances-db", views.BalancesDb, name="getBalancesFromDb"),
    path("balances-db/<int:id>", views.BalancesDb, name="getBalance"),

]
