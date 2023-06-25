from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.
def index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    nSlides = n//3 + ceil((n/3) - (n//3))
    params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'product': products}
    print(params)
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return HttpResponse('we are at contact page')


def tracker(request):
    return HttpResponse('we are at tracker page')

def search(request):
    return HttpResponse('we are at search page')

def productView(request):
    return HttpResponse('we are at product view page')

def checkout(request):
    return HttpResponse('we are at check out page')