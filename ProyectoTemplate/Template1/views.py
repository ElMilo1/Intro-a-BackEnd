from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse

# Create your views here.

def renderTemplate(request):
    return render(request,'Template1/Hola_Mundo.html')

def renderTemplate2(request):
    data = {'nombre' : 'Milo'}
    return render(request,'Template1/Implementando_Data.html',data)

def renderTemplate3(request):
    data = {'ID':'123','Nombre':'Milo','mail':'milo@hotmail.cl'}
    return render(request,'Template1/UserInfoTemp.html',data)