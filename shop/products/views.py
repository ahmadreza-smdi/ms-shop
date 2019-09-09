from django.shortcuts import render
from .models import Product
from user.models import Purchase,Customer
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Create your views here.

def show_product(request):
    c = Product.objects.all()
    c_length = len(c)
    return render(request,'product.html',{'c':c},{'clen':c_length})

@login_required
def buy_product(request):
    username = request.user.get_username()
    return render(request,'dashboard.html')
