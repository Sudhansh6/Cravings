from django.shortcuts import render, redirect
from .models import item, address
from django.contrib.auth.models import User
from django.contrib import messages
from django import forms


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
    flag = True
    if len(items)==0:
        flag = False
    sum = 0 
    for i in items:
        sum += i.price
    context = {
        'items': items,
        'sum':sum,
        'flag' : flag
    }
    return render(request, "cart.html", context)


def checkout(request):
    items = item.objects.filter(user=request.user)
    if request.method == "POST":
        if not address.objects.filter(id=request.POST['old']).exists():
            street = request.POST['street']
            city = request.POST['city']
            state = request.POST['state']
            pin = request.POST['pin']
            phone = request.POST['phone']
            name = request.POST['name']
            new = address(street=street,city=city,state=state,
                name=name,pin=pin,phone=phone,user=request.user)
            new.save()
            messages.info(request, "Address successfully added")
            return redirect('/cart/checkout')
        items.delete()
        messages.info(request, "Order successfully placed :)")
        return redirect('/')

    user_address = address.objects.filter(user=request.user)
    sum = 0
    delivery = 30
    for i in items:
        sum += i.price
    taxes = 0.18*sum
    total = sum + delivery  + taxes
    context = {
        'items': items,
        'sum': sum,
        'delivery': delivery,
        'taxes': taxes,
        'total': total,
        'address' : user_address
    }
    return render(request, "checkout.html", context)
