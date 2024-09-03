from django.shortcuts import render
from django.http import HttpRequest , HttpResponse

# Create your views here.

def Home(request):
    data ={'nombrePagina':'Home'}
    return render(request,'tienda/Home.html',data)