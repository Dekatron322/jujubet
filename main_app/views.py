from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from . import views
from django.urls import reverse
import requests
import json
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, login, logout
from main_app.models import UserProfile
from main_app.forms import SignUpForm, MessageForm, AdvertForm, GamesForm, AdvertUpdateForm, MatchForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):

    ads = Advert.objects.all().order_by('-id')[:2]

    footer = Advert.objects.all().order_by('-id')[1:9]

    big = Advert.objects.all().order_by('-id')[3:4]

    side = Advert.objects.all().order_by('-id')[5:7]

    sides = Advert.objects.all().order_by('-id')[7:8]

    games = VipGames.objects.all()

    #url = "https://api.sofascore.com/api/v1/unique-tournament/17/season/37036/standings/total"

    #payload = ""

    #headers = {
        #'cookie': "__cfduid=d784ae9d9a4af12ae1d8f525636e03ccc1619367812",
        #'authority': "api.sofascore.com",
        #"cache-control": "max-age-0",
        #"sec-ch-ua": "^\^"
    #}

    #response = requests.request("GET", url, data=payload, headers=headers)
    #data = response.json()

    #standings = data['standings']

    context = {'ads': ads, 'big':big, 'side':side, 'sides':sides, 'footer':footer, 'games':games}
    return render(request, 'main_app/index.html', context)
@login_required(login_url='/signin')
def faq(request):
   
    return render(request, 'main_app/faq.html')

@login_required(login_url='/signin')
def about(request):
    footer = Advert.objects.all().order_by('-id')[1:9]

    context = {'footer': footer}
    return render(request, 'main_app/about.html', context)

def predict(request):
    footer = Advert.objects.all().order_by('-id')[1:9]

    context = {"footer": footer}
    return render(request, 'main_app/predict.html', )

@login_required(login_url='/signin')
def vip_game(request):
    games = VipGames.objects.all()
    footer = Advert.objects.all().order_by('-id')[1:9]
    context = {'games': games, "footer":footer}
   
    return render(request, 'main_app/vip.html', context)


def contact(request):
    footer = Advert.objects.all().order_by('-id')[1:9]
    form = ContactForm(request.POST)
    context = {'form':form, "footer":footer}
    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')
            try:
                data = Contact()
                data.name = name
                data.email = email
                data.phone = phone
                data.subject = subject
                data.message = message
                data.ip = request.META.get('REMOTE_ADDR')
                data.save()
                messages.success(request, "Your message has been delivered")
                return redirect(reverse('contact'))
            except:
                messages.error(request, "Could Not Add This Advert" )
                return HttpResponseRedirect('/contact')
        else:
            messages.warning(request, form.errors)

    return render(request, 'main_app/contact.html', context)


def contact_message(request):
    recieved = Contact.objects.all()
    footer = Advert.objects.all().order_by('-id')[1:9]
    context = {'recieved': recieved, "footer":footer}
    return render(request, 'main_app/contact_message.html', context)


def subscribe(request):
    footer = Advert.objects.all().order_by('-id')[1:9]
    context = {"footer":footer}
    return render(request, 'main_app/subscribe.html', context)

def livescores(request):

    import requests

    url = "https://api.sofascore.com/api/v1/sport/football/scheduled-events/2021-09-15"

    payload = ""

    headers = {
        'cookie': "__cfduid=d784ae9d9a4af12ae1d8f525636e03ccc1619367812",
        'authority': "api.sofascore.com",
        "cache-control": "max-age-0",
        "sec-ch-ua": "^\^"
    }

    response = requests.request("GET", url, data=payload, headers=headers)
    data = response.json()

    events = data['events']

       
    return render(request, 'main_app/livescores.html', {'events':events})


def policy(request):
    footer = Advert.objects.all().order_by('-id')[1:9]
    context = {"footer":footer}

    return render(request, 'main_app/policy.html', context)

# admin dashboard
def boss(request):
    vip = VipGames.objects.all()
    total_users = UserProfile.objects.all().count()
    total_vip_games = VipGames.objects.all().count()
    total_ads = Advert.objects.all().count()
    messages_revieved = Message.objects.all().count()



    context = {"total_users": total_users, "total_vip_games":total_vip_games, "total_ads":total_ads, "messages_revieved":messages_revieved}
    return render(request, 'main_app/admin_page.html', context)


### admin place adverts
def ads(request):
    form = AdvertForm(request.POST, request.FILES)

    context = {'form':form}
    if request.method == 'POST':
        
        if form.is_valid():    
            title = form.cleaned_data.get('title')
            link = form.cleaned_data.get('link')
            image = request.FILES['image']

            try:
                data = Advert()
                data.title = title
                data.link = link
                data.image = image

                data.save()
                messages.success(request, "Successfully Placed")
                return redirect(reverse('ads'))
            except:
                messages.error(request, "Could Not Add This Advert" )
                return HttpResponseRedirect('/ads')

        else:
            messages.warning(request, form.errors)
    return render(request, 'main_app/ads.html', context)

### admin list of adverts
def manage_advert(request):
    my_advert = Advert.objects.all()

    context = {'my_advert': my_advert}
    return render(request, 'main_app/manage_advert.html', context)

    
    return render(request, "main_app/ads.html", context)  



def edit_advert(request, pk):
    queryset = Advert.objects.get(id=pk)
    form = AdvertUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = AdvertUpdateForm(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'updated')
            return redirect('/manage_advert')

    context = {
        'form':form
    }

    return render(request, "main_app/edit_advert.html", context)


### admin delete message
def delete_advert(request, id):
    advert = get_object_or_404(Advert, id=id)
    advert.delete()
    messages.success(request, "advert deleted successfully!")
    return redirect(reverse('manage_advert'))   



#### admin construct message
def message(request):
    url = request.META.get('HTTP_REFERER')
    form = MessageForm(request.POST)
    context = {'form':form}
    if request.method == 'POST':
        
        if  form.is_valid():
            title = form.cleaned_data.get('title')
            message = form.cleaned_data.get('message')
            try:
                data = Message()
                data.title = title
                data.message = message

                data.save()
                messages.success(request, "Message Sent")
                return redirect(reverse('message'))
            except:
                messages.warning(request, form.errors)
                return HttpResponseRedirect('/message')
        else:
            messages.warning(request, form.errors)
    
    return render(request, 'main_app/message.html', context)



### admin list of messages
def manage_message(request):
    sent = Message.objects.all()

    context = {'sent':sent}
    return render(request, 'main_app/manage_message.html', context)

### admin edit message 
def edit_message(request, message_id):
    instance = get_object_or_404(Message, id=message_id)
    form = MessageForm(request.POST or None, instance=instance)
    context = {
        'form': form,
        'message_id': message_id,
        'page_title': 'Edit Message'
    }
    if request.method == 'POST':
        
        if form.is_valid():
            title = form.cleaned_data.get('title')
            message = form.cleaned_data.get('message')
            try:

                data = Message.objects.get(id=message_id)
                data.title = title
                data.message = message
                data.save()
                messages.success(request, "Message Sent")
            except:
                messages.warning(request, form.errors)

        else:
            messages.warning(request, form.errors)
            
    return render(request, 'main_app/edit_message.html', context)


### admin delete message
def delete_message(request, id):
    message = get_object_or_404(Message, id=id)
    message.delete()
    messages.success(request, "message deleted successfully!")
    return redirect(reverse('manage_message'))



def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "welcome onboard "+user.username)
            current_user = request.user
            userprofile = UserProfile.objects.get(user_id = current_user.id)
            request.session['userimage'] = userprofile.image.url
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "Login Error !! username or password is incorrect")
            return HttpResponseRedirect('/signin')
    current_user = request.user
    
    context = {
    }
    return render(request, 'main_app/signin.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            user = authenticate(username=username, password=password)
            login(request, user)
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id

            data.image="images.png"
            data.save()
            messages.success(request, 'Account successfully created')
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect('/signup')
    form = SignUpForm()

    context = {'form':form,  }
    return render(request, 'main_app/signup.html', context)

def logout_func(request):
    logout(request)
    messages.success(request, 'Logged out')
    return HttpResponseRedirect('/')



#### admin construct message
def games(request):
    url = request.META.get('HTTP_REFERER')
    results = VipGames.objects.all()
    form = GamesForm(request.POST)
    context = {'form':form, 'results':results}
    if request.method == 'POST':
        
        if  form.is_valid():
            home_team = form.cleaned_data.get('home_team')
            away_team = form.cleaned_data.get('away_team')
            league = form.cleaned_data.get('league')
            tip = form.cleaned_data.get('tip')
            odds = form.cleaned_data.get('odds')
            #result = form.cleaned_data.get('result')
            try:
                data = VipGames()
                data.home_team = home_team
                data.away_team = away_team
                data.league = league
                data.tip = tip
                data.odds = odds
                #data.result = result
                data.save()
                messages.success(request, "Game Sent Successfully")
                return redirect(reverse('games'))
            except:
                messages.warning(request, form.errors)
                return HttpResponseRedirect('/games')
        else:
            messages.warning(request, form.errors)
    
    return render(request, 'main_app/games.html', context)

### admin list of games
def manage_games(request):
    my_games = VipGames.objects.all()

    context = {'my_games': my_games }
    return render(request, 'main_app/manage_games.html', context)


def edit_game(request, game_id):
    instance = get_object_or_404(VipGames, id=game_id)
    form = MatchForm(request.POST or None, instance=instance)
    context = {
        'form': form,
        'game_id': game_id,
        'games':games,
        'page_title': 'Edit Game'
    }
    if request.method == 'POST':
        
        if form.is_valid():
            home_team = form.cleaned_data.get('home_team')
            away_team = form.cleaned_data.get('away_team')
            league = form.cleaned_data.get('league')
            tip = form.cleaned_data.get('tip')
            odds = form.cleaned_data.get('odds')
            result = form.cleaned_data.get('result')
            try:
                data = VipGames.objects.get(id=game_id)
                data.home_team = home_team
                data.away_team = away_team
                data.league = league
                data.tip = tip
                data.odds = odds
                data.result = result
                data.save()
                messages.success(request, "Done")
            except:
                messages.warning(request, form.errors)

        else:
            messages.warning(request, form.errors)
            
    return render(request, 'main_app/edit_game.html', context)

### admin delete message
def delete_game(request, id):
    game = get_object_or_404(VipGames, id=id)
    game.delete()
    messages.success(request, "game deleted successfully!")
    return redirect(reverse('manage_games'))
