from django.shortcuts import render, redirect
from .models import item
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def index(request):
    if request.method == 'POST':
        deleted_item = request.POST['id']
        print(deleted_item)
        x = item.objects.get(pk=int(deleted_item))
        x.delete()
        return redirect('/cart')
    if request.user.is_anonymous:
        messages.info(request, "You need to login before viewing cart")
        return redirect('/accounts/login')
    items = item.objects.filter(user=request.user)
    sum = 0 
    for i in items:
        sum += i.price
    context = {
        'items': items,
        'sum':sum,
    }
    return render(request, "cart.html", context)

def checkout(request):
    tip = 0 
    items = item.objects.filter(user=request.user)
    sum = 0
    delivery = 30
    for i in items:
        sum += i.price
    taxes = 0.18*sum
    if request.method == 'POST':
        pass
    total = sum + delivery + tip + taxes
    context = {
        'items': items,
        'sum': sum,
        'delivery': delivery,
        'taxes': taxes,
        'total': total
    }
    return render(request, "checkout.html", context)
