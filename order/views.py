from django.shortcuts import render
from .models import Order, Transaction
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def buy(request, order_id):
    
    return render(request, 'order/buy.html', {'order_id': order_id})


def failure(request, order_id):
    return render(request, 'order/failure.html', {'order_id': order_id})

def success(request, order_id):
    return render(request, 'order/success.html', {'order_id': order_id})