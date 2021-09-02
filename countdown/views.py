from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from . import views
from django.urls import reverse
# Create your views here.


def index(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            data = Subscribe()
            data.email = form.cleaned_data['email']

            data.save()
            messages.success(request, "Your message has been delivered")
            return HttpResponseRedirect(reverse("countdown"))
        else:
            messages.success(request, "error occured")
            return HttpResponseRedirect(reverse("countdown"))

    form = ContactForm
    
    context = {'form':form}
   
    return render(request, 'countdown/countdown.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = Contact()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.phone = form.cleaned_data['phone']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Your message has been delivered")
            return HttpResponseRedirect(reverse("contact"))

    form = ContactForm
    
    context = {'form':form}
    return render(request, 'countdown/contact.html', context)

def about(request):
    
    return render(request, 'countdown/about.html')
