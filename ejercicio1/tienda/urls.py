from django.contrib import admin
from django.urls import path , include
from tienda import views as tienda

urlpatterns = {
    path('',tienda.Home),
    path('electro/',tienda.Electro)
}