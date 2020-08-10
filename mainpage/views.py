from django.shortcuts import render, redirect
from .models import item
from cart.models import item as user_item
from django.contrib.auth.models import User
from django.contrib import messages
from django import forms

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

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send email code goes here
            messages.info(request, "Thank you for contacting us :)")
            return redirect('/contact')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
