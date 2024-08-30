from django.contrib import admin
from django.urls import path
from Template1 import views as temp1

urlpatterns = [
    path('Temp/',temp1.renderTemplate),
    path('Temp1/',temp1.renderTemplate2),
    path('info/',temp1.renderTemplate3)
]