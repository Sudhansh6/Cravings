from django.shortcuts import render, redirect
from .models import item
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        messages.info(request, "You need to login before viewing cart")
        return redirect('/accounts/login')
    items = item.objects.filter(user=request.user)
    context = {
        'items': items
    }
    return render(request, "cart.html", context)
