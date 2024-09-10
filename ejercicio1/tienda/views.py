from django.shortcuts import render
from django.http import HttpRequest , HttpResponse

# Create your views here.

def Home(request):
    return render(request,'tienda/Home.html')

def Electro(request):
    data = {'productCategory':'Electro',
            'imgProduct1':'HDD1TB-BLUE.png',
            'productName1':'HDD WesterDigital blue 1TB',
            'imgProduct2':'nvmem21t.png'}
    return render(request,'tienda/Product.html',data)
