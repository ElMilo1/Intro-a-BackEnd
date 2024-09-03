from django.contrib import admin
from django.urls import path , include
from tienda import views

urlpatterns = {
    path('',views.Home)
}