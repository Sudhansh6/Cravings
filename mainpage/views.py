from django.shortcuts import render, redirect
from .models import item
from cart.models import item as user_item
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'POST':
        if request.user.is_anonymous:
            messages.info(request, "You need to login before adding items to cart")
            return redirect('/accounts/login')
        added_item = request.POST['id']
        a = item.objects.get(pk=int(added_item))
        new = user_item(name = a.name, price = a.price,img = a.img, description = a.description, user=request.user)
        new.save()
        return redirect('/')
    context = {
        'items': item.objects.all(),
    }
    return render(request, "index.html",context)
