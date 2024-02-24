from django.shortcuts import render
from . import models

#---------------------------------------------------------------------------------
#------------------------ SINGLE PAGE VIEW ---------------------------------------
#---------------------------------------------------------------------------------
def home_view(request):
    products=models.Product.objects.all()
    return render(request,'ecom/index.html',{'products':products})

def gallery_view(request):
    products=models.Product.objects.all()
    return render(request,'ecom/gallery.html',{'products':products})

def allproducts_view(request):
    products=models.Product.objects.all()
    return render(request,'ecom/allproducts.html',{'products':products})

def single_product_view(request,pk):
    product=models.Product.objects.get(id=pk)
    return render(request,'ecom/single_product.html',{'product':product})