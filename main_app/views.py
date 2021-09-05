from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from . import views
from django.urls import reverse
import requests
import json
# Create your views here.


def index(request):
   
    return render(request, 'main_app/index.html')

def faq(request):
   
    return render(request, 'main_app/faq.html')

def about(request):
   
    return render(request, 'main_app/about.html')

def predict(request):
   
    return render(request, 'main_app/predict.html')


def signup(request):
   
    return render(request, 'main_app/signup.html')


def signin(request):
   
    return render(request, 'main_app/signin.html')

def vip(request):
   
    return render(request, 'main_app/vip.html')

def contact(request):
   
    return render(request, 'main_app/contact.html')

def subscribe(request):
   
    return render(request, 'main_app/subscribe.html')

def livescores(request):    
    return render(request, 'main_app/livescores.html')

def vip(request):
    return render(request, 'main_app/vip.html')

def policy(request):
    return render(request, 'main_app/policy.html')

