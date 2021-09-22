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
    sent = Message.objects.all().order_by('-id')[:1]

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

    context = {'ads': ads, 'big':big, 'side':side, 'sides':sides, 'footer':footer, 'games':games, "sent":sent}
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
    games = VipGames.objects.all().order_by('-id')[:1]
    footer = Advert.objects.all().order_by('-id')[1:9]
    sent = Message.objects.all().order_by('-id')[:1]
    context = {'games': games, "footer":footer, "sent":sent}
   
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

            a_home_team = form.cleaned_data.get('a_home_team')
            a_away_team = form.cleaned_data.get('a_away_team')
            a_league = form.cleaned_data.get('a_league')
            a_tip = form.cleaned_data.get('a_tip')
            a_odds = form.cleaned_data.get('a_odds')

            b_home_team = form.cleaned_data.get('b_home_team')
            b_away_team = form.cleaned_data.get('b_away_team')
            b_league = form.cleaned_data.get('b_league')
            b_tip = form.cleaned_data.get('b_tip')
            b_odds = form.cleaned_data.get('b_odds')

            c_home_team = form.cleaned_data.get('c_home_team')
            c_away_team = form.cleaned_data.get('c_away_team')
            c_league = form.cleaned_data.get('c_league')
            c_tip = form.cleaned_data.get('c_tip')
            c_odds = form.cleaned_data.get('c_odds')

            d_home_team = form.cleaned_data.get('d_home_team')
            d_away_team = form.cleaned_data.get('d_away_team')
            d_league = form.cleaned_data.get('d_league')
            d_tip = form.cleaned_data.get('d_tip')
            d_odds = form.cleaned_data.get('d_odds')

            # double predictions
            dA_home_team = form.cleaned_data.get('dA_home_team')
            dA_away_team = form.cleaned_data.get('dA_away_team')
            dA_league = form.cleaned_data.get('dA_league')
            dA_tip = form.cleaned_data.get('dA_tip')
            dA_odds = form.cleaned_data.get('dA_odds')

            dB_home_team = form.cleaned_data.get('dB_home_team')
            dB_away_team = form.cleaned_data.get('dB_away_team')
            dB_league = form.cleaned_data.get('dB_league')
            dB_tip = form.cleaned_data.get('dB_tip')
            dB_odds = form.cleaned_data.get('dB_odds')

            ## multiple odds 1/3
            tA_home_team = form.cleaned_data.get('tA_home_team')
            tA_away_team = form.cleaned_data.get('tA_away_team')
            tA_league = form.cleaned_data.get('tA_league')
            tA_tip = form.cleaned_data.get('tA_tip')
            tA_odds = form.cleaned_data.get('tA_odds')

            tB_home_team = form.cleaned_data.get('tB_home_team')
            tB_away_team = form.cleaned_data.get('tB_away_team')
            tB_league = form.cleaned_data.get('tB_league')
            tB_tip = form.cleaned_data.get('tB_tip')
            tB_odds = form.cleaned_data.get('tB_odds')

            tC_home_team = form.cleaned_data.get('tC_home_team')
            tC_away_team = form.cleaned_data.get('tC_away_team')
            tC_league = form.cleaned_data.get('tC_league')
            tC_tip = form.cleaned_data.get('tC_tip')
            tC_odds = form.cleaned_data.get('tC_odds')

            ## multiple odds 1/4
            fA_home_team = form.cleaned_data.get('fA_home_team')
            fA_away_team = form.cleaned_data.get('fA_away_team')
            fA_league = form.cleaned_data.get('fA_league')
            fA_tip = form.cleaned_data.get('fA_tip')
            fA_odds = form.cleaned_data.get('fA_odds')

            fB_home_team = form.cleaned_data.get('fB_home_team')
            fB_away_team = form.cleaned_data.get('fB_away_team')
            fB_league = form.cleaned_data.get('fB_league')
            fB_tip = form.cleaned_data.get('fB_tip')
            fB_odds = form.cleaned_data.get('fB_odds')

            fC_home_team = form.cleaned_data.get('fC_home_team')
            fC_away_team = form.cleaned_data.get('fC_away_team')
            fC_league = form.cleaned_data.get('fC_league')
            fC_tip = form.cleaned_data.get('fC_tip')
            fC_odds = form.cleaned_data.get('fC_odds')

            fD_home_team = form.cleaned_data.get('fD_home_team')
            fD_away_team = form.cleaned_data.get('fD_away_team')
            fD_league = form.cleaned_data.get('fD_league')
            fD_tip = form.cleaned_data.get('fD_tip')
            fD_odds = form.cleaned_data.get('fD_odds')


            ## multiple odds 1/5
            ffA_home_team = form.cleaned_data.get('ffA_home_team')
            ffA_away_team = form.cleaned_data.get('ffA_away_team')
            ffA_league = form.cleaned_data.get('ffA_league')
            ffA_tip = form.cleaned_data.get('ffA_tip')
            ffA_odds = form.cleaned_data.get('ffA_odds')

            ffB_home_team = form.cleaned_data.get('ffB_home_team')
            ffB_away_team = form.cleaned_data.get('ffB_away_team')
            ffB_league = form.cleaned_data.get('ffB_league')
            ffB_tip = form.cleaned_data.get('ffB_tip')
            ffB_odds = form.cleaned_data.get('ffB_odds')

            ffC_home_team = form.cleaned_data.get('ffC_home_team')
            ffC_away_team = form.cleaned_data.get('ffC_away_team')
            ffC_league = form.cleaned_data.get('ffC_league')
            ffC_tip = form.cleaned_data.get('ffC_tip')
            ffC_odds = form.cleaned_data.get('ffC_odds')

            ffD_home_team = form.cleaned_data.get('ffD_home_team')
            ffD_away_team = form.cleaned_data.get('ffD_away_team')
            ffD_league = form.cleaned_data.get('ffD_league')
            ffD_tip = form.cleaned_data.get('ffD_tip')
            ffD_odds = form.cleaned_data.get('ffD_odds')

            ffE_home_team = form.cleaned_data.get('ffE_home_team')
            ffE_away_team = form.cleaned_data.get('ffE_away_team')
            ffE_league = form.cleaned_data.get('ffE_league')
            ffE_tip = form.cleaned_data.get('ffE_tip')
            ffE_odds = form.cleaned_data.get('ffE_odds')


            ## multiple odds 1/6
            siA_home_team = form.cleaned_data.get('siA_home_team')
            siA_away_team = form.cleaned_data.get('siA_away_team')
            siA_league = form.cleaned_data.get('siA_league')
            siA_tip = form.cleaned_data.get('siA_tip')
            siA_odds = form.cleaned_data.get('siA_odds')

            siB_home_team = form.cleaned_data.get('siB_home_team')
            siB_away_team = form.cleaned_data.get('siB_away_team')
            siB_league = form.cleaned_data.get('siB_league')
            siB_tip = form.cleaned_data.get('siB_tip')
            siB_odds = form.cleaned_data.get('siB_odds')

            siC_home_team = form.cleaned_data.get('siC_home_team')
            siC_away_team = form.cleaned_data.get('siC_away_team')
            siC_league = form.cleaned_data.get('siC_league')
            siC_tip = form.cleaned_data.get('siC_tip')
            siC_odds = form.cleaned_data.get('siC_odds')

            siD_home_team = form.cleaned_data.get('siD_home_team')
            siD_away_team = form.cleaned_data.get('siD_away_team')
            siD_league = form.cleaned_data.get('siD_league')
            siD_tip = form.cleaned_data.get('siD_tip')
            siD_odds = form.cleaned_data.get('siD_odds')

            siE_home_team = form.cleaned_data.get('siE_home_team')
            siE_away_team = form.cleaned_data.get('siE_away_team')
            siE_league = form.cleaned_data.get('siE_league')
            siE_tip = form.cleaned_data.get('siE_tip')
            siE_odds = form.cleaned_data.get('siE_odds')

            siF_home_team = form.cleaned_data.get('siF_home_team')
            siF_away_team = form.cleaned_data.get('siF_away_team')
            siF_league = form.cleaned_data.get('siF_league')
            siF_tip = form.cleaned_data.get('siF_tip')
            siF_odds = form.cleaned_data.get('siF_odds')


            ## multiple odds 1/7
            sA_home_team = form.cleaned_data.get('sA_home_team')
            sA_away_team = form.cleaned_data.get('sA_away_team')
            sA_league = form.cleaned_data.get('sA_league')
            sA_tip = form.cleaned_data.get('sA_tip')
            sA_odds = form.cleaned_data.get('sA_odds')

            sB_home_team = form.cleaned_data.get('sB_home_team')
            sB_away_team = form.cleaned_data.get('sB_away_team')
            sB_league = form.cleaned_data.get('sB_league')
            sB_tip = form.cleaned_data.get('sB_tip')
            sB_odds = form.cleaned_data.get('sB_odds')

            sC_home_team = form.cleaned_data.get('sC_home_team')
            sC_away_team = form.cleaned_data.get('sC_away_team')
            sC_league = form.cleaned_data.get('sC_league')
            sC_tip = form.cleaned_data.get('sC_tip')
            sC_odds = form.cleaned_data.get('sC_odds')

            sD_home_team = form.cleaned_data.get('sD_home_team')
            sD_away_team = form.cleaned_data.get('sD_away_team')
            sD_league = form.cleaned_data.get('sD_league')
            sD_tip = form.cleaned_data.get('sD_tip')
            sD_odds = form.cleaned_data.get('sD_odds')

            sE_home_team = form.cleaned_data.get('sE_home_team')
            sE_away_team = form.cleaned_data.get('sE_away_team')
            sE_league = form.cleaned_data.get('sE_league')
            sE_tip = form.cleaned_data.get('sE_tip')
            sE_odds = form.cleaned_data.get('sE_odds')

            sF_home_team = form.cleaned_data.get('sF_home_team')
            sF_away_team = form.cleaned_data.get('sF_away_team')
            sF_league = form.cleaned_data.get('sF_league')
            sF_tip = form.cleaned_data.get('sF_tip')
            sF_odds = form.cleaned_data.get('sF_odds')

            gF_home_team = form.cleaned_data.get('gF_home_team')
            gF_away_team = form.cleaned_data.get('gF_away_team')
            gF_league = form.cleaned_data.get('gF_league')
            gF_tip = form.cleaned_data.get('gF_tip')
            gF_odds = form.cleaned_data.get('gF_odds')


            ## both teams to score (gg)
            ggA_home_team = form.cleaned_data.get('ggA_home_team')
            ggA_away_team = form.cleaned_data.get('ggA_away_team')
            ggA_league = form.cleaned_data.get('ggA_league')
            ggA_tip = form.cleaned_data.get('ggA_tip')
            ggA_odds = form.cleaned_data.get('ggA_odds')

            ggB_home_team = form.cleaned_data.get('ggB_home_team')
            ggB_away_team = form.cleaned_data.get('ggB_away_team')
            ggB_league = form.cleaned_data.get('ggB_league')
            ggB_tip = form.cleaned_data.get('ggB_tip')
            ggB_odds = form.cleaned_data.get('ggB_odds')

            ggC_home_team = form.cleaned_data.get('ggC_home_team')
            ggC_away_team = form.cleaned_data.get('ggC_away_team')
            ggC_league = form.cleaned_data.get('ggC_league')
            ggC_tip = form.cleaned_data.get('ggC_tip')
            ggC_odds = form.cleaned_data.get('ggC_odds')

            ggD_home_team = form.cleaned_data.get('ggD_home_team')
            ggD_away_team = form.cleaned_data.get('ggD_away_team')
            ggD_league = form.cleaned_data.get('ggD_league')
            ggD_tip = form.cleaned_data.get('ggD_tip')
            ggD_odds = form.cleaned_data.get('ggD_odds')

            ggE_home_team = form.cleaned_data.get('ggE_home_team')
            ggE_away_team = form.cleaned_data.get('ggE_away_team')
            ggE_league = form.cleaned_data.get('ggE_league')
            ggE_tip = form.cleaned_data.get('ggE_tip')
            ggE_odds = form.cleaned_data.get('ggE_odds')

            ggF_home_team = form.cleaned_data.get('ggF_home_team')
            ggF_away_team = form.cleaned_data.get('ggF_away_team')
            ggF_league = form.cleaned_data.get('ggF_league')
            ggF_tip = form.cleaned_data.get('ggF_tip')
            ggF_odds = form.cleaned_data.get('ggF_odds')


            ggG_home_team = form.cleaned_data.get('ggG_home_team')
            ggG_away_team = form.cleaned_data.get('ggG_away_team')
            ggG_league = form.cleaned_data.get('ggG_league')
            ggG_tip = form.cleaned_data.get('ggG_tip')
            ggG_odds = form.cleaned_data.get('ggG_odds')

            ggH_home_team = form.cleaned_data.get('ggH_home_team')
            ggH_away_team = form.cleaned_data.get('ggH_away_team')
            ggH_league = form.cleaned_data.get('ggH_league')
            ggH_tip = form.cleaned_data.get('ggH_tip')
            ggH_odds = form.cleaned_data.get('ggH_odds')

            ggI_home_team = form.cleaned_data.get('ggI_home_team')
            ggI_away_team = form.cleaned_data.get('ggI_away_team')
            ggI_league = form.cleaned_data.get('ggI_league')
            ggI_tip = form.cleaned_data.get('ggI_tip')
            ggI_odds = form.cleaned_data.get('ggI_odds')


            ggJ_home_team = form.cleaned_data.get('ggJ_home_team')
            ggJ_away_team = form.cleaned_data.get('ggJ_away_team')
            ggJ_league = form.cleaned_data.get('ggJ_league')
            ggJ_tip = form.cleaned_data.get('ggJ_tip')
            ggJ_odds = form.cleaned_data.get('ggJ_odds')


            #correct Score

            ccA_home_team = form.cleaned_data.get('ccA_home_team')
            ccA_away_team = form.cleaned_data.get('ccA_away_team')
            ccA_league = form.cleaned_data.get('ccA_league')
            ccA_tip = form.cleaned_data.get('ccA_tip')
            ccA_odds = form.cleaned_data.get('ccA_odds')

            ccB_home_team = form.cleaned_data.get('ccB_home_team')
            ccB_away_team = form.cleaned_data.get('ccB_away_team')
            ccB_league = form.cleaned_data.get('ccB_league')
            ccB_tip = form.cleaned_data.get('ccB_tip')
            ccB_odds = form.cleaned_data.get('ccB_odds')

            ccC_home_team = form.cleaned_data.get('ccC_home_team')
            ccC_away_team = form.cleaned_data.get('ccC_away_team')
            ccC_league = form.cleaned_data.get('ccC_league')
            ccC_tip = form.cleaned_data.get('ccC_tip')
            ccC_odds = form.cleaned_data.get('ccC_odds')

            ccD_home_team = form.cleaned_data.get('ccD_home_team')
            ccD_away_team = form.cleaned_data.get('ccD_away_team')
            ccD_league = form.cleaned_data.get('ccD_league')
            ccD_tip = form.cleaned_data.get('ccD_tip')
            ccD_odds = form.cleaned_data.get('ccD_odds')

            ccE_home_team = form.cleaned_data.get('ccE_home_team')
            ccE_away_team = form.cleaned_data.get('ccE_away_team')
            ccE_league = form.cleaned_data.get('ccE_league')
            ccE_tip = form.cleaned_data.get('ccE_tip')
            ccE_odds = form.cleaned_data.get('ccE_odds')


            ccF_home_team = form.cleaned_data.get('ccF_home_team')
            ccF_away_team = form.cleaned_data.get('ccF_away_team')
            ccF_league = form.cleaned_data.get('ccF_league')
            ccF_tip = form.cleaned_data.get('ccF_tip')
            ccF_odds = form.cleaned_data.get('ccF_odds')

            ccG_home_team = form.cleaned_data.get('ccG_home_team')
            ccG_away_team = form.cleaned_data.get('ccG_away_team')
            ccG_league = form.cleaned_data.get('ccG_league')
            ccG_tip = form.cleaned_data.get('ccG_tip')
            ccG_odds = form.cleaned_data.get('ccG_odds')

            ccH_home_team = form.cleaned_data.get('ccH_home_team')
            ccH_away_team = form.cleaned_data.get('ccH_away_team')
            ccH_league = form.cleaned_data.get('ccH_league')
            ccH_tip = form.cleaned_data.get('ccH_tip')
            ccH_odds = form.cleaned_data.get('ccH_odds')

            ccI_home_team = form.cleaned_data.get('ccI_home_team')
            ccI_away_team = form.cleaned_data.get('ccI_away_team')
            ccI_league = form.cleaned_data.get('ccI_league')
            ccI_tip = form.cleaned_data.get('ccI_tip')
            ccI_odds = form.cleaned_data.get('ccI_odds')


            ccJ_home_team = form.cleaned_data.get('ccJ_home_team')
            ccJ_away_team = form.cleaned_data.get('ccJ_away_team')
            ccJ_league = form.cleaned_data.get('ccJ_league')
            ccJ_tip = form.cleaned_data.get('ccJ_tip')
            ccJ_odds = form.cleaned_data.get('ccJ_odds')

            ## half time predict

            htA_home_team = form.cleaned_data.get('htA_home_team')
            htA_away_team = form.cleaned_data.get('htA_away_team')
            htA_league = form.cleaned_data.get('htA_league')
            htA_tip = form.cleaned_data.get('htA_tip')
            htA_odds = form.cleaned_data.get('htA_odds')

            htB_home_team = form.cleaned_data.get('htB_home_team')
            htB_away_team = form.cleaned_data.get('htB_away_team')
            htB_league = form.cleaned_data.get('htB_league')
            htB_tip = form.cleaned_data.get('htB_tip')
            htB_odds = form.cleaned_data.get('htB_odds')

            htC_home_team = form.cleaned_data.get('htC_home_team')
            htC_away_team = form.cleaned_data.get('htC_away_team')
            htC_league = form.cleaned_data.get('htC_league')
            htC_tip = form.cleaned_data.get('htC_tip')
            htC_odds = form.cleaned_data.get('htC_odds')

            htD_home_team = form.cleaned_data.get('htD_home_team')
            htD_away_team = form.cleaned_data.get('htD_away_team')
            htD_league = form.cleaned_data.get('htD_league')
            htD_tip = form.cleaned_data.get('htD_tip')
            htD_odds = form.cleaned_data.get('htD_odds')

            htE_home_team = form.cleaned_data.get('htE_home_team')
            htE_away_team = form.cleaned_data.get('htE_away_team')
            htE_league = form.cleaned_data.get('htE_league')
            htE_tip = form.cleaned_data.get('htE_tip')
            htE_odds = form.cleaned_data.get('htE_odds')

            htF_home_team = form.cleaned_data.get('htF_home_team')
            htF_away_team = form.cleaned_data.get('htF_away_team')
            htF_league = form.cleaned_data.get('htF_league')
            htF_tip = form.cleaned_data.get('htF_tip')
            htF_odds = form.cleaned_data.get('htF_odds')


            htG_home_team = form.cleaned_data.get('htG_home_team')
            htG_away_team = form.cleaned_data.get('htG_away_team')
            htG_league = form.cleaned_data.get('htG_league')
            htG_tip = form.cleaned_data.get('htG_tip')
            htG_odds = form.cleaned_data.get('htG_odds')

            htH_home_team = form.cleaned_data.get('htH_home_team')
            htH_away_team = form.cleaned_data.get('htH_away_team')
            htH_league = form.cleaned_data.get('htH_league')
            htH_tip = form.cleaned_data.get('htH_tip')
            htH_odds = form.cleaned_data.get('htH_odds')

            htI_home_team = form.cleaned_data.get('htI_home_team')
            htI_away_team = form.cleaned_data.get('htI_away_team')
            htI_league = form.cleaned_data.get('htI_league')
            htI_tip = form.cleaned_data.get('htI_tip')
            htI_odds = form.cleaned_data.get('htI_odds')


            htJ_home_team = form.cleaned_data.get('htJ_home_team')
            htJ_away_team = form.cleaned_data.get('htJ_away_team')
            htJ_league = form.cleaned_data.get('htJ_league')
            htJ_tip = form.cleaned_data.get('htJ_tip')
            htJ_odds = form.cleaned_data.get('htJ_odds')

            ## full time

            ftA_home_team = form.cleaned_data.get('ftA_home_team')
            ftA_away_team = form.cleaned_data.get('ftA_away_team')
            ftA_league = form.cleaned_data.get('ftA_league')
            ftA_tip = form.cleaned_data.get('ftA_tip')
            ftA_odds = form.cleaned_data.get('ftA_odds')

            ftB_home_team = form.cleaned_data.get('ftB_home_team')
            ftB_away_team = form.cleaned_data.get('ftB_away_team')
            ftB_league = form.cleaned_data.get('ftB_league')
            ftB_tip = form.cleaned_data.get('ftB_tip')
            ftB_odds = form.cleaned_data.get('ftB_odds')

            ftC_home_team = form.cleaned_data.get('ftC_home_team')
            ftC_away_team = form.cleaned_data.get('ftC_away_team')
            ftC_league = form.cleaned_data.get('ftC_league')
            ftC_tip = form.cleaned_data.get('ftC_tip')
            ftC_odds = form.cleaned_data.get('ftC_odds')

            ftD_home_team = form.cleaned_data.get('ftD_home_team')
            ftD_away_team = form.cleaned_data.get('ftD_away_team')
            ftD_league = form.cleaned_data.get('ftD_league')
            ftD_tip = form.cleaned_data.get('ftD_tip')
            ftD_odds = form.cleaned_data.get('ftD_odds')

            ftE_home_team = form.cleaned_data.get('ftE_home_team')
            ftE_away_team = form.cleaned_data.get('ftE_away_team')
            ftE_league = form.cleaned_data.get('ftE_league')
            ftE_tip = form.cleaned_data.get('ftE_tip')
            ftE_odds = form.cleaned_data.get('ftE_odds')

            ftF_home_team = form.cleaned_data.get('ftF_home_team')
            ftF_away_team = form.cleaned_data.get('ftF_away_team')
            ftF_league = form.cleaned_data.get('ftF_league')
            ftF_tip = form.cleaned_data.get('ftF_tip')
            ftF_odds = form.cleaned_data.get('ftF_odds')

            ftG_home_team = form.cleaned_data.get('ftG_home_team')
            ftG_away_team = form.cleaned_data.get('ftG_away_team')
            ftG_league = form.cleaned_data.get('ftG_league')
            ftG_tip = form.cleaned_data.get('ftG_tip')
            ftG_odds = form.cleaned_data.get('ftG_odds')

            ftH_home_team = form.cleaned_data.get('ftH_home_team')
            ftH_away_team = form.cleaned_data.get('ftH_away_team')
            ftH_league = form.cleaned_data.get('ftH_league')
            ftH_tip = form.cleaned_data.get('ftH_tip')
            ftH_odds = form.cleaned_data.get('ftH_odds')

            ftI_home_team = form.cleaned_data.get('ftI_home_team')
            ftI_away_team = form.cleaned_data.get('ftI_away_team')
            ftI_league = form.cleaned_data.get('ftI_league')
            ftI_tip = form.cleaned_data.get('ftI_tip')
            ftI_odds = form.cleaned_data.get('ftI_odds')


            ftJ_home_team = form.cleaned_data.get('ftJ_home_team')
            ftJ_away_team = form.cleaned_data.get('ftJ_away_team')
            ftJ_league = form.cleaned_data.get('ftJ_league')
            ftJ_tip = form.cleaned_data.get('ftJ_tip')
            ftJ_odds = form.cleaned_data.get('ftJ_odds')

            #result = form.cleaned_data.get('result')
            try:
                data = VipGames()
                data.home_team = home_team
                data.away_team = away_team
                data.league = league
                data.tip = tip
                data.odds = odds

                data.a_home_team = a_home_team
                data.a_away_team = a_away_team
                data.a_league = a_league
                data.a_tip = a_tip
                data.a_odds = a_odds

                data.b_home_team = b_home_team
                data.b_away_team = b_away_team
                data.b_league = b_league
                data.b_tip = b_tip
                data.b_odds = b_odds

                data.c_home_team = c_home_team
                data.c_away_team = c_away_team
                data.c_league = c_league
                data.c_tip = c_tip
                data.c_odds = c_odds

                data.d_home_team = d_home_team
                data.d_away_team = d_away_team
                data.d_league = d_league
                data.d_tip = d_tip
                data.d_odds = d_odds


                ## double predictions
                data.dA_home_team = dA_home_team
                data.dA_away_team = dA_away_team
                data.dA_league = dA_league
                data.dA_tip = dA_tip
                data.dA_odds = dA_odds

                data.dB_home_team = dB_home_team
                data.dB_away_team = dB_away_team
                data.dB_league = dB_league
                data.dB_tip = dB_tip
                data.dB_odds = dB_odds

                ## multiple prediction 1/3

                data.tA_home_team = tA_home_team
                data.tA_away_team = tA_away_team
                data.tA_league = tA_league
                data.tA_tip = tA_tip
                data.tA_odds = tA_odds

                data.tB_home_team = tB_home_team
                data.tB_away_team = tB_away_team
                data.tB_league = tB_league
                data.tB_tip = tB_tip
                data.tB_odds = tB_odds

                data.tC_home_team = tC_home_team
                data.tC_away_team = tC_away_team
                data.tC_league = tC_league
                data.tC_tip = tC_tip
                data.tC_odds = tC_odds

                ## multiple prediction 1/4

                data.fA_home_team = fA_home_team
                data.fA_away_team = fA_away_team
                data.fA_league = fA_league
                data.fA_tip = fA_tip
                data.fA_odds = fA_odds

                data.fB_home_team = fB_home_team
                data.fB_away_team = fB_away_team
                data.fB_league = fB_league
                data.fB_tip = fB_tip
                data.fB_odds = fB_odds

                data.fC_home_team = fC_home_team
                data.fC_away_team = fC_away_team
                data.fC_league = fC_league
                data.fC_tip = fC_tip
                data.fC_odds = fC_odds

                data.fD_home_team = fD_home_team
                data.fD_away_team = fD_away_team
                data.fD_league = fD_league
                data.fD_tip = fD_tip
                data.fD_odds = fD_odds

                ## multiple prediction 1/5

                data.ffA_home_team = ffA_home_team
                data.ffA_away_team = ffA_away_team
                data.ffA_league = ffA_league
                data.ffA_tip = ffA_tip
                data.ffA_odds = ffA_odds

                data.ffB_home_team = ffB_home_team
                data.ffB_away_team = ffB_away_team
                data.ffB_league = ffB_league
                data.ffB_tip = ffB_tip
                data.ffB_odds = ffB_odds

                data.ffC_home_team = ffC_home_team
                data.ffC_away_team = ffC_away_team
                data.ffC_league = ffC_league
                data.ffC_tip = ffC_tip
                data.ffC_odds = ffC_odds

                data.ffD_home_team = ffD_home_team
                data.ffD_away_team = ffD_away_team
                data.ffD_league = ffD_league
                data.ffD_tip = ffD_tip
                data.ffD_odds = ffD_odds

                data.ffE_home_team = ffE_home_team
                data.ffE_away_team = ffE_away_team
                data.ffE_league = ffE_league
                data.ffE_tip = ffE_tip
                data.ffE_odds = ffE_odds


                ## multiple prediction 1/6

                data.siA_home_team = siA_home_team
                data.siA_away_team = siA_away_team
                data.siA_league = siA_league
                data.siA_tip = siA_tip
                data.siA_odds = siA_odds

                data.siB_home_team = siB_home_team
                data.siB_away_team = siB_away_team
                data.siB_league = siB_league
                data.siB_tip = siB_tip
                data.siB_odds = siB_odds

                data.siC_home_team = siC_home_team
                data.siC_away_team = siC_away_team
                data.siC_league = siC_league
                data.siC_tip = siC_tip
                data.siC_odds = siC_odds

                data.siD_home_team = siD_home_team
                data.siD_away_team = siD_away_team
                data.siD_league = siD_league
                data.siD_tip = siD_tip
                data.siD_odds = siD_odds

                data.siE_home_team = siE_home_team
                data.siE_away_team = siE_away_team
                data.siE_league = siE_league
                data.siE_tip = siE_tip
                data.siE_odds = siE_odds

                data.siF_home_team = siF_home_team
                data.siF_away_team = siF_away_team
                data.siF_league = siF_league
                data.siF_tip = siF_tip
                data.siF_odds = siF_odds

                ## multiple prediction 1/7

                data.sA_home_team = sA_home_team
                data.sA_away_team = sA_away_team
                data.sA_league = sA_league
                data.sA_tip = sA_tip
                data.sA_odds = sA_odds

                data.sB_home_team = sB_home_team
                data.sB_away_team = sB_away_team
                data.sB_league = sB_league
                data.sB_tip = sB_tip
                data.sB_odds = sB_odds

                data.sC_home_team = sC_home_team
                data.sC_away_team = sC_away_team
                data.sC_league = sC_league
                data.sC_tip = sC_tip
                data.sC_odds = sC_odds

                data.sD_home_team = sD_home_team
                data.sD_away_team = sD_away_team
                data.sD_league = sD_league
                data.sD_tip = sD_tip
                data.sD_odds = sD_odds

                data.sE_home_team = sE_home_team
                data.sE_away_team = sE_away_team
                data.sE_league = sE_league
                data.sE_tip = sE_tip
                data.sE_odds = sE_odds

                data.sF_home_team = sF_home_team
                data.sF_away_team = sF_away_team
                data.sF_league = sF_league
                data.sF_tip = sF_tip
                data.sF_odds = sF_odds

                data.gF_home_team = gF_home_team
                data.gF_away_team = gF_away_team
                data.gF_league = gF_league
                data.gF_tip = gF_tip
                data.gF_odds = gF_odds

                ## both teams to score (gg)

                data.ggA_home_team = ggA_home_team
                data.ggA_away_team = ggA_away_team
                data.ggA_league = ggA_league
                data.ggA_tip = ggA_tip
                data.ggA_odds = ggA_odds

                data.ggB_home_team = ggB_home_team
                data.ggB_away_team = ggB_away_team
                data.ggB_league = ggB_league
                data.ggB_tip = ggB_tip
                data.ggB_odds = ggB_odds

                data.ggC_home_team = ggC_home_team
                data.ggC_away_team = ggC_away_team
                data.ggC_league = ggC_league
                data.ggC_tip = ggC_tip
                data.ggC_odds = ggC_odds

                data.ggD_home_team = ggD_home_team
                data.ggD_away_team = ggD_away_team
                data.ggD_league = ggD_league
                data.ggD_tip = ggD_tip
                data.ggD_odds = ggD_odds

                data.ggE_home_team = ggE_home_team
                data.ggE_away_team = ggE_away_team
                data.ggE_league = ggE_league
                data.ggE_tip = ggE_tip
                data.ggE_odds = ggE_odds

                data.ggF_home_team = ggF_home_team
                data.ggF_away_team = ggF_away_team
                data.ggF_league = ggF_league
                data.ggF_tip = ggF_tip
                data.ggF_odds = ggF_odds

                data.ggG_home_team = ggG_home_team
                data.ggG_away_team = ggG_away_team
                data.ggG_league = ggG_league
                data.ggG_tip = ggG_tip
                data.ggG_odds = ggG_odds

                data.ggH_home_team = ggH_home_team
                data.ggH_away_team = ggH_away_team
                data.ggH_league = ggH_league
                data.ggH_tip = ggH_tip
                data.ggH_odds = ggH_odds

                data.ggI_home_team = ggI_home_team
                data.ggI_away_team = ggI_away_team
                data.ggI_league = ggI_league
                data.ggI_tip = ggI_tip
                data.ggI_odds = ggI_odds

                data.ggJ_home_team = ggJ_home_team
                data.ggJ_away_team = ggJ_away_team
                data.ggJ_league = ggJ_league
                data.ggJ_tip = ggJ_tip
                data.ggJ_odds = ggJ_odds


                ## correct score (cc)

                data.ccA_home_team = ccA_home_team
                data.ccA_away_team = ccA_away_team
                data.ccA_league = ccA_league
                data.ccA_tip = ccA_tip
                data.ccA_odds = ccA_odds

                data.ccB_home_team = ccB_home_team
                data.ccB_away_team = ccB_away_team
                data.ccB_league = ccB_league
                data.ccB_tip = ccB_tip
                data.ccB_odds = ccB_odds

                data.ccC_home_team = ccC_home_team
                data.ccC_away_team = ccC_away_team
                data.ccC_league = ccC_league
                data.ccC_tip = ccC_tip
                data.ccC_odds = ccC_odds

                data.ccD_home_team = ccD_home_team
                data.ccD_away_team = ccD_away_team
                data.ccD_league = ccD_league
                data.ccD_tip = ccD_tip
                data.ccD_odds = ccD_odds

                data.ccE_home_team = ccE_home_team
                data.ccE_away_team = ccE_away_team
                data.ccE_league = ccE_league
                data.ccE_tip = ccE_tip
                data.ccE_odds = ccE_odds

                data.ccF_home_team = ccF_home_team
                data.ccF_away_team = ccF_away_team
                data.ccF_league = ccF_league
                data.ccF_tip = ccF_tip
                data.ccF_odds = ccF_odds

                data.ccG_home_team = ccG_home_team
                data.ccG_away_team = ccG_away_team
                data.ccG_league = ccG_league
                data.ccG_tip = ccG_tip
                data.ccG_odds = ccG_odds

                data.ccH_home_team = ccH_home_team
                data.ccH_away_team = ccH_away_team
                data.ccH_league = ccH_league
                data.ccH_tip = ccH_tip
                data.ccH_odds = ccH_odds

                data.ccI_home_team = ccI_home_team
                data.ccI_away_team = ccI_away_team
                data.ccI_league = ccI_league
                data.ccI_tip = ccI_tip
                data.ccI_odds = ccI_odds

                data.ccJ_home_team = ccJ_home_team
                data.ccJ_away_team = ccJ_away_team
                data.ccJ_league = ccJ_league
                data.ccJ_tip = ccJ_tip
                data.ccJ_odds = ccJ_odds

                ## half-time score (ht)

                data.htA_home_team = htA_home_team
                data.htA_away_team = htA_away_team
                data.htA_league = htA_league
                data.htA_tip = htA_tip
                data.htA_odds = htA_odds

                data.htB_home_team = htB_home_team
                data.htB_away_team = htB_away_team
                data.htB_league = htB_league
                data.htB_tip = htB_tip
                data.htB_odds = htB_odds

                data.htC_home_team = htC_home_team
                data.htC_away_team = htC_away_team
                data.htC_league = htC_league
                data.htC_tip = htC_tip
                data.htC_odds = htC_odds

                data.htD_home_team = htD_home_team
                data.htD_away_team = htD_away_team
                data.htD_league = htD_league
                data.htD_tip = htD_tip
                data.htD_odds = htD_odds

                data.htE_home_team = htE_home_team
                data.htE_away_team = htE_away_team
                data.htE_league = htE_league
                data.htE_tip = htE_tip
                data.htE_odds = htE_odds

                data.htF_home_team = htF_home_team
                data.htF_away_team = htF_away_team
                data.htF_league = htF_league
                data.htF_tip = htF_tip
                data.htF_odds = htF_odds

                data.htG_home_team = htG_home_team
                data.htG_away_team = htG_away_team
                data.htG_league = htG_league
                data.htG_tip = htG_tip
                data.htG_odds = htG_odds

                data.htH_home_team = htH_home_team
                data.htH_away_team = htH_away_team
                data.htH_league = htH_league
                data.htH_tip = htH_tip
                data.htH_odds = htH_odds

                data.htI_home_team = htI_home_team
                data.htI_away_team = htI_away_team
                data.htI_league = htI_league
                data.htI_tip = htI_tip
                data.htI_odds = htI_odds

                data.htJ_home_team = htJ_home_team
                data.htJ_away_team = htJ_away_team
                data.htJ_league = htJ_league
                data.htJ_tip = htJ_tip
                data.htJ_odds = htJ_odds


                ## full-time score (ft)

                data.ftA_home_team = ftA_home_team
                data.ftA_away_team = ftA_away_team
                data.ftA_league = ftA_league
                data.ftA_tip = ftA_tip
                data.ftA_odds = ftA_odds

                data.ftB_home_team = ftB_home_team
                data.ftB_away_team = ftB_away_team
                data.ftB_league = ftB_league
                data.ftB_tip = ftB_tip
                data.ftB_odds = ftB_odds

                data.ftC_home_team = ftC_home_team
                data.ftC_away_team = ftC_away_team
                data.ftC_league = ftC_league
                data.ftC_tip = ftC_tip
                data.ftC_odds = ftC_odds

                data.ftD_home_team = ftD_home_team
                data.ftD_away_team = ftD_away_team
                data.ftD_league = ftD_league
                data.ftD_tip = ftD_tip
                data.ftD_odds = ftD_odds

                data.ftE_home_team = ftE_home_team
                data.ftE_away_team = ftE_away_team
                data.ftE_league = ftE_league
                data.ftE_tip = ftE_tip
                data.ftE_odds = ftE_odds

                data.ftF_home_team = ftF_home_team
                data.ftF_away_team = ftF_away_team
                data.ftF_league = ftF_league
                data.ftF_tip = ftF_tip
                data.ftF_odds = ftF_odds

                data.ftG_home_team = ftG_home_team
                data.ftG_away_team = ftG_away_team
                data.ftG_league = ftG_league
                data.ftG_tip = ftG_tip
                data.ftG_odds = ftG_odds

                data.ftH_home_team = ftH_home_team
                data.ftH_away_team = ftH_away_team
                data.ftH_league = ftH_league
                data.ftH_tip = ftH_tip
                data.ftH_odds = ftH_odds

                data.ftI_home_team = ftI_home_team
                data.ftI_away_team = ftI_away_team
                data.ftI_league = ftI_league
                data.ftI_tip = ftI_tip
                data.ftI_odds = ftI_odds

                data.ftJ_home_team = ftJ_home_team
                data.ftJ_away_team = ftJ_away_team
                data.ftJ_league = ftJ_league
                data.ftJ_tip = ftJ_tip
                data.ftJ_odds = ftJ_odds

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
    my_games = VipGames.objects.all().order_by('-id')

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

            a_home_team = form.cleaned_data.get('a_home_team')
            a_away_team = form.cleaned_data.get('a_away_team')
            a_league = form.cleaned_data.get('a_league')
            a_tip = form.cleaned_data.get('a_tip')
            a_odds = form.cleaned_data.get('a_odds')
            a_result = form.cleaned_data.get('a_result')

            b_home_team = form.cleaned_data.get('b_home_team')
            b_away_team = form.cleaned_data.get('b_away_team')
            b_league = form.cleaned_data.get('b_league')
            b_tip = form.cleaned_data.get('b_tip')
            b_odds = form.cleaned_data.get('b_odds')
            b_result = form.cleaned_data.get('b_result')

            c_home_team = form.cleaned_data.get('c_home_team')
            c_away_team = form.cleaned_data.get('c_away_team')
            c_league = form.cleaned_data.get('c_league')
            c_tip = form.cleaned_data.get('c_tip')
            c_odds = form.cleaned_data.get('c_odds')
            c_result = form.cleaned_data.get('c_result')

            d_home_team = form.cleaned_data.get('d_home_team')
            d_away_team = form.cleaned_data.get('d_away_team')
            d_league = form.cleaned_data.get('d_league')
            d_tip = form.cleaned_data.get('d_tip')
            d_odds = form.cleaned_data.get('d_odds')
            d_result = form.cleaned_data.get('d_result')

            # double predictions
            dA_home_team = form.cleaned_data.get('dA_home_team')
            dA_away_team = form.cleaned_data.get('dA_away_team')
            dA_league = form.cleaned_data.get('dA_league')
            dA_tip = form.cleaned_data.get('dA_tip')
            dA_odds = form.cleaned_data.get('dA_odds')
            dA_result = form.cleaned_data.get('dA_result')

            dB_home_team = form.cleaned_data.get('dB_home_team')
            dB_away_team = form.cleaned_data.get('dB_away_team')
            dB_league = form.cleaned_data.get('dB_league')
            dB_tip = form.cleaned_data.get('dB_tip')
            dB_odds = form.cleaned_data.get('dB_odds')
            dB_result = form.cleaned_data.get('dB_result')

            ## multiple odds 1/3
            tA_home_team = form.cleaned_data.get('tA_home_team')
            tA_away_team = form.cleaned_data.get('tA_away_team')
            tA_league = form.cleaned_data.get('tA_league')
            tA_tip = form.cleaned_data.get('tA_tip')
            tA_odds = form.cleaned_data.get('tA_odds')
            tA_result = form.cleaned_data.get('tA_result')

            tB_home_team = form.cleaned_data.get('tB_home_team')
            tB_away_team = form.cleaned_data.get('tB_away_team')
            tB_league = form.cleaned_data.get('tB_league')
            tB_tip = form.cleaned_data.get('tB_tip')
            tB_odds = form.cleaned_data.get('tB_odds')
            tB_result = form.cleaned_data.get('tB_result')

            tC_home_team = form.cleaned_data.get('tC_home_team')
            tC_away_team = form.cleaned_data.get('tC_away_team')
            tC_league = form.cleaned_data.get('tC_league')
            tC_tip = form.cleaned_data.get('tC_tip')
            tC_odds = form.cleaned_data.get('tC_odds')
            tC_result = form.cleaned_data.get('tC_result')

            ## multiple odds 1/4
            fA_home_team = form.cleaned_data.get('fA_home_team')
            fA_away_team = form.cleaned_data.get('fA_away_team')
            fA_league = form.cleaned_data.get('fA_league')
            fA_tip = form.cleaned_data.get('fA_tip')
            fA_odds = form.cleaned_data.get('fA_odds')
            fA_result = form.cleaned_data.get('fA_result')

            fB_home_team = form.cleaned_data.get('fB_home_team')
            fB_away_team = form.cleaned_data.get('fB_away_team')
            fB_league = form.cleaned_data.get('fB_league')
            fB_tip = form.cleaned_data.get('fB_tip')
            fB_odds = form.cleaned_data.get('fB_odds')
            fB_result = form.cleaned_data.get('fB_result')

            fC_home_team = form.cleaned_data.get('fC_home_team')
            fC_away_team = form.cleaned_data.get('fC_away_team')
            fC_league = form.cleaned_data.get('fC_league')
            fC_tip = form.cleaned_data.get('fC_tip')
            fC_odds = form.cleaned_data.get('fC_odds')
            fC_result = form.cleaned_data.get('fC_result')

            fD_home_team = form.cleaned_data.get('fD_home_team')
            fD_away_team = form.cleaned_data.get('fD_away_team')
            fD_league = form.cleaned_data.get('fD_league')
            fD_tip = form.cleaned_data.get('fD_tip')
            fD_odds = form.cleaned_data.get('fD_odds')
            fD_result = form.cleaned_data.get('fD_result')


            ## multiple odds 1/5
            ffA_home_team = form.cleaned_data.get('ffA_home_team')
            ffA_away_team = form.cleaned_data.get('ffA_away_team')
            ffA_league = form.cleaned_data.get('ffA_league')
            ffA_tip = form.cleaned_data.get('ffA_tip')
            ffA_odds = form.cleaned_data.get('ffA_odds')
            ffA_result = form.cleaned_data.get('ffA_result')

            ffB_home_team = form.cleaned_data.get('ffB_home_team')
            ffB_away_team = form.cleaned_data.get('ffB_away_team')
            ffB_league = form.cleaned_data.get('ffB_league')
            ffB_tip = form.cleaned_data.get('ffB_tip')
            ffB_odds = form.cleaned_data.get('ffB_odds')
            ffB_result = form.cleaned_data.get('ffB_result')

            ffC_home_team = form.cleaned_data.get('ffC_home_team')
            ffC_away_team = form.cleaned_data.get('ffC_away_team')
            ffC_league = form.cleaned_data.get('ffC_league')
            ffC_tip = form.cleaned_data.get('ffC_tip')
            ffC_odds = form.cleaned_data.get('ffC_odds')
            ffC_result = form.cleaned_data.get('ffC_result')

            ffD_home_team = form.cleaned_data.get('ffD_home_team')
            ffD_away_team = form.cleaned_data.get('ffD_away_team')
            ffD_league = form.cleaned_data.get('ffD_league')
            ffD_tip = form.cleaned_data.get('ffD_tip')
            ffD_odds = form.cleaned_data.get('ffD_odds')
            ffD_result = form.cleaned_data.get('ffD_result')

            ffE_home_team = form.cleaned_data.get('ffE_home_team')
            ffE_away_team = form.cleaned_data.get('ffE_away_team')
            ffE_league = form.cleaned_data.get('ffE_league')
            ffE_tip = form.cleaned_data.get('ffE_tip')
            ffE_odds = form.cleaned_data.get('ffE_odds')
            ffE_result = form.cleaned_data.get('ffE_result')


            ## multiple odds 1/6
            siA_home_team = form.cleaned_data.get('siA_home_team')
            siA_away_team = form.cleaned_data.get('siA_away_team')
            siA_league = form.cleaned_data.get('siA_league')
            siA_tip = form.cleaned_data.get('siA_tip')
            siA_odds = form.cleaned_data.get('siA_odds')
            siA_result = form.cleaned_data.get('siA_result')

            siB_home_team = form.cleaned_data.get('siB_home_team')
            siB_away_team = form.cleaned_data.get('siB_away_team')
            siB_league = form.cleaned_data.get('siB_league')
            siB_tip = form.cleaned_data.get('siB_tip')
            siB_odds = form.cleaned_data.get('siB_odds')
            siB_result = form.cleaned_data.get('siB_result')

            siC_home_team = form.cleaned_data.get('siC_home_team')
            siC_away_team = form.cleaned_data.get('siC_away_team')
            siC_league = form.cleaned_data.get('siC_league')
            siC_tip = form.cleaned_data.get('siC_tip')
            siC_odds = form.cleaned_data.get('siC_odds')
            siC_result = form.cleaned_data.get('siC_result')

            siD_home_team = form.cleaned_data.get('siD_home_team')
            siD_away_team = form.cleaned_data.get('siD_away_team')
            siD_league = form.cleaned_data.get('siD_league')
            siD_tip = form.cleaned_data.get('siD_tip')
            siD_odds = form.cleaned_data.get('siD_odds')
            siD_result = form.cleaned_data.get('siD_result')

            siE_home_team = form.cleaned_data.get('siE_home_team')
            siE_away_team = form.cleaned_data.get('siE_away_team')
            siE_league = form.cleaned_data.get('siE_league')
            siE_tip = form.cleaned_data.get('siE_tip')
            siE_odds = form.cleaned_data.get('siE_odds')
            siE_result = form.cleaned_data.get('siE_result')

            siF_home_team = form.cleaned_data.get('siF_home_team')
            siF_away_team = form.cleaned_data.get('siF_away_team')
            siF_league = form.cleaned_data.get('siF_league')
            siF_tip = form.cleaned_data.get('siF_tip')
            siF_odds = form.cleaned_data.get('siF_odds')
            siF_result = form.cleaned_data.get('siF_result')


            ## multiple odds 1/7
            sA_home_team = form.cleaned_data.get('sA_home_team')
            sA_away_team = form.cleaned_data.get('sA_away_team')
            sA_league = form.cleaned_data.get('sA_league')
            sA_tip = form.cleaned_data.get('sA_tip')
            sA_odds = form.cleaned_data.get('sA_odds')
            sA_result = form.cleaned_data.get('sA_result')

            sB_home_team = form.cleaned_data.get('sB_home_team')
            sB_away_team = form.cleaned_data.get('sB_away_team')
            sB_league = form.cleaned_data.get('sB_league')
            sB_tip = form.cleaned_data.get('sB_tip')
            sB_odds = form.cleaned_data.get('sB_odds')
            sB_result = form.cleaned_data.get('sB_result')

            sC_home_team = form.cleaned_data.get('sC_home_team')
            sC_away_team = form.cleaned_data.get('sC_away_team')
            sC_league = form.cleaned_data.get('sC_league')
            sC_tip = form.cleaned_data.get('sC_tip')
            sC_odds = form.cleaned_data.get('sC_odds')
            sC_result = form.cleaned_data.get('sC_result')

            sD_home_team = form.cleaned_data.get('sD_home_team')
            sD_away_team = form.cleaned_data.get('sD_away_team')
            sD_league = form.cleaned_data.get('sD_league')
            sD_tip = form.cleaned_data.get('sD_tip')
            sD_odds = form.cleaned_data.get('sD_odds')
            sD_result = form.cleaned_data.get('sD_result')

            sE_home_team = form.cleaned_data.get('sE_home_team')
            sE_away_team = form.cleaned_data.get('sE_away_team')
            sE_league = form.cleaned_data.get('sE_league')
            sE_tip = form.cleaned_data.get('sE_tip')
            sE_odds = form.cleaned_data.get('sE_odds')
            sE_result = form.cleaned_data.get('sE_result')

            sF_home_team = form.cleaned_data.get('sF_home_team')
            sF_away_team = form.cleaned_data.get('sF_away_team')
            sF_league = form.cleaned_data.get('sF_league')
            sF_tip = form.cleaned_data.get('sF_tip')
            sF_odds = form.cleaned_data.get('sF_odds')
            SF_result = form.cleaned_data.get('sF_result')

            gF_home_team = form.cleaned_data.get('gF_home_team')
            gF_away_team = form.cleaned_data.get('gF_away_team')
            gF_league = form.cleaned_data.get('gF_league')
            gF_tip = form.cleaned_data.get('gF_tip')
            gF_odds = form.cleaned_data.get('gF_odds')
            gf_result = form.cleaned_data.get('gF_result')


            ## both teams to score (gg)
            ggA_home_team = form.cleaned_data.get('ggA_home_team')
            ggA_away_team = form.cleaned_data.get('ggA_away_team')
            ggA_league = form.cleaned_data.get('ggA_league')
            ggA_tip = form.cleaned_data.get('ggA_tip')
            ggA_odds = form.cleaned_data.get('ggA_odds')
            ggA_result = form.cleaned_data.get('ggA_result')


            ggB_home_team = form.cleaned_data.get('ggB_home_team')
            ggB_away_team = form.cleaned_data.get('ggB_away_team')
            ggB_league = form.cleaned_data.get('ggB_league')
            ggB_tip = form.cleaned_data.get('ggB_tip')
            ggB_odds = form.cleaned_data.get('ggB_odds')
            ggB_result = form.cleaned_data.get('ggB_result')

            ggC_home_team = form.cleaned_data.get('ggC_home_team')
            ggC_away_team = form.cleaned_data.get('ggC_away_team')
            ggC_league = form.cleaned_data.get('ggC_league')
            ggC_tip = form.cleaned_data.get('ggC_tip')
            ggC_odds = form.cleaned_data.get('ggC_odds')
            ggC_result = form.cleaned_data.get('ggC_result')

            ggD_home_team = form.cleaned_data.get('ggD_home_team')
            ggD_away_team = form.cleaned_data.get('ggD_away_team')
            ggD_league = form.cleaned_data.get('ggD_league')
            ggD_tip = form.cleaned_data.get('ggD_tip')
            ggD_odds = form.cleaned_data.get('ggD_odds')
            ggD_result = form.cleaned_data.get('ggD_result')

            ggE_home_team = form.cleaned_data.get('ggE_home_team')
            ggE_away_team = form.cleaned_data.get('ggE_away_team')
            ggE_league = form.cleaned_data.get('ggE_league')
            ggE_tip = form.cleaned_data.get('ggE_tip')
            ggE_odds = form.cleaned_data.get('ggE_odds')
            ggE_result = form.cleaned_data.get('ggE_result')

            ggF_home_team = form.cleaned_data.get('ggF_home_team')
            ggF_away_team = form.cleaned_data.get('ggF_away_team')
            ggF_league = form.cleaned_data.get('ggF_league')
            ggF_tip = form.cleaned_data.get('ggF_tip')
            ggF_odds = form.cleaned_data.get('ggF_odds')
            ggF_result = form.cleaned_data.get('ggF_result')


            ggG_home_team = form.cleaned_data.get('ggG_home_team')
            ggG_away_team = form.cleaned_data.get('ggG_away_team')
            ggG_league = form.cleaned_data.get('ggG_league')
            ggG_tip = form.cleaned_data.get('ggG_tip')
            ggG_odds = form.cleaned_data.get('ggG_odds')
            ggG_result = form.cleaned_data.get('ggG_result')


            ggH_home_team = form.cleaned_data.get('ggH_home_team')
            ggH_away_team = form.cleaned_data.get('ggH_away_team')
            ggH_league = form.cleaned_data.get('ggH_league')
            ggH_tip = form.cleaned_data.get('ggH_tip')
            ggH_odds = form.cleaned_data.get('ggH_odds')
            ggH_result = form.cleaned_data.get('ggH_result')

            ggI_home_team = form.cleaned_data.get('ggI_home_team')
            ggI_away_team = form.cleaned_data.get('ggI_away_team')
            ggI_league = form.cleaned_data.get('ggI_league')
            ggI_tip = form.cleaned_data.get('ggI_tip')
            ggI_odds = form.cleaned_data.get('ggI_odds')
            ggI_result = form.cleaned_data.get('ggI_result')


            ggJ_home_team = form.cleaned_data.get('ggJ_home_team')
            ggJ_away_team = form.cleaned_data.get('ggJ_away_team')
            ggJ_league = form.cleaned_data.get('ggJ_league')
            ggJ_tip = form.cleaned_data.get('ggJ_tip')
            ggJ_odds = form.cleaned_data.get('ggJ_odds')
            ggJ_result = form.cleaned_data.get('ggJ_result')


            #correct Score

            ccA_home_team = form.cleaned_data.get('ccA_home_team')
            ccA_away_team = form.cleaned_data.get('ccA_away_team')
            ccA_league = form.cleaned_data.get('ccA_league')
            ccA_tip = form.cleaned_data.get('ccA_tip')
            ccA_odds = form.cleaned_data.get('ccA_odds')
            ccA_result = form.cleaned_data.get('ccA_result')

            ccB_home_team = form.cleaned_data.get('ccB_home_team')
            ccB_away_team = form.cleaned_data.get('ccB_away_team')
            ccB_league = form.cleaned_data.get('ccB_league')
            ccB_tip = form.cleaned_data.get('ccB_tip')
            ccB_odds = form.cleaned_data.get('ccB_odds')
            ccB_result = form.cleaned_data.get('ccB_result')

            ccC_home_team = form.cleaned_data.get('ccC_home_team')
            ccC_away_team = form.cleaned_data.get('ccC_away_team')
            ccC_league = form.cleaned_data.get('ccC_league')
            ccC_tip = form.cleaned_data.get('ccC_tip')
            ccC_odds = form.cleaned_data.get('ccC_odds')
            ccC_result = form.cleaned_data.get('ccC_result')

            ccD_home_team = form.cleaned_data.get('ccD_home_team')
            ccD_away_team = form.cleaned_data.get('ccD_away_team')
            ccD_league = form.cleaned_data.get('ccD_league')
            ccD_tip = form.cleaned_data.get('ccD_tip')
            ccD_odds = form.cleaned_data.get('ccD_odds')
            ccD_result = form.cleaned_data.get('ccD_result')

            ccE_home_team = form.cleaned_data.get('ccE_home_team')
            ccE_away_team = form.cleaned_data.get('ccE_away_team')
            ccE_league = form.cleaned_data.get('ccE_league')
            ccE_tip = form.cleaned_data.get('ccE_tip')
            ccE_odds = form.cleaned_data.get('ccE_odds')
            ccE_result = form.cleaned_data.get('ccE_result')

            ccF_home_team = form.cleaned_data.get('ccF_home_team')
            ccF_away_team = form.cleaned_data.get('ccF_away_team')
            ccF_league = form.cleaned_data.get('ccF_league')
            ccF_tip = form.cleaned_data.get('ccF_tip')
            ccF_odds = form.cleaned_data.get('ccF_odds')
            ccF_result = form.cleaned_data.get('ccF_result')


            ccG_home_team = form.cleaned_data.get('ccG_home_team')
            ccG_away_team = form.cleaned_data.get('ccG_away_team')
            ccG_league = form.cleaned_data.get('ccG_league')
            ccG_tip = form.cleaned_data.get('ccG_tip')
            ccG_odds = form.cleaned_data.get('ccG_odds')
            ccG_result = form.cleaned_data.get('ccG_result')

            ccH_home_team = form.cleaned_data.get('ccH_home_team')
            ccH_away_team = form.cleaned_data.get('ccH_away_team')
            ccH_league = form.cleaned_data.get('ccH_league')
            ccH_tip = form.cleaned_data.get('ccH_tip')
            ccH_odds = form.cleaned_data.get('ccH_odds')
            ccH_result = form.cleaned_data.get('ccH_result')

            ccI_home_team = form.cleaned_data.get('ccI_home_team')
            ccI_away_team = form.cleaned_data.get('ccI_away_team')
            ccI_league = form.cleaned_data.get('ccI_league')
            ccI_tip = form.cleaned_data.get('ccI_tip')
            ccI_odds = form.cleaned_data.get('ccI_odds')
            ccI_result = form.cleaned_data.get('ccI_result')


            ccJ_home_team = form.cleaned_data.get('ccJ_home_team')
            ccJ_away_team = form.cleaned_data.get('ccJ_away_team')
            ccJ_league = form.cleaned_data.get('ccJ_league')
            ccJ_tip = form.cleaned_data.get('ccJ_tip')
            ccJ_odds = form.cleaned_data.get('ccJ_odds')
            ccJ_result = form.cleaned_data.get('ccJ_result')

            ## half time predict

            htA_home_team = form.cleaned_data.get('htA_home_team')
            htA_away_team = form.cleaned_data.get('htA_away_team')
            htA_league = form.cleaned_data.get('htA_league')
            htA_tip = form.cleaned_data.get('htA_tip')
            htA_odds = form.cleaned_data.get('htA_odds')
            htA_result = form.cleaned_data.get('htA_result')

            htB_home_team = form.cleaned_data.get('htB_home_team')
            htB_away_team = form.cleaned_data.get('htB_away_team')
            htB_league = form.cleaned_data.get('htB_league')
            htB_tip = form.cleaned_data.get('htB_tip')
            htB_odds = form.cleaned_data.get('htB_odds')
            htB_result = form.cleaned_data.get('htB_result')


            htC_home_team = form.cleaned_data.get('htC_home_team')
            htC_away_team = form.cleaned_data.get('htC_away_team')
            htC_league = form.cleaned_data.get('htC_league')
            htC_tip = form.cleaned_data.get('htC_tip')
            htC_odds = form.cleaned_data.get('htC_odds')
            htC_result = form.cleaned_data.get('htC_result')

            htD_home_team = form.cleaned_data.get('htD_home_team')
            htD_away_team = form.cleaned_data.get('htD_away_team')
            htD_league = form.cleaned_data.get('htD_league')
            htD_tip = form.cleaned_data.get('htD_tip')
            htD_odds = form.cleaned_data.get('htD_odds')
            htD_result = form.cleaned_data.get('htD_result')

            htE_home_team = form.cleaned_data.get('htE_home_team')
            htE_away_team = form.cleaned_data.get('htE_away_team')
            htE_league = form.cleaned_data.get('htE_league')
            htE_tip = form.cleaned_data.get('htE_tip')
            htE_odds = form.cleaned_data.get('htE_odds')
            htE_result = form.cleaned_data.get('htE_result')

            htF_home_team = form.cleaned_data.get('htF_home_team')
            htF_away_team = form.cleaned_data.get('htF_away_team')
            htF_league = form.cleaned_data.get('htF_league')
            htF_tip = form.cleaned_data.get('htF_tip')
            htF_odds = form.cleaned_data.get('htF_odds')
            htF_result = form.cleaned_data.get('htF_result')

            htG_home_team = form.cleaned_data.get('htG_home_team')
            htG_away_team = form.cleaned_data.get('htG_away_team')
            htG_league = form.cleaned_data.get('htG_league')
            htG_tip = form.cleaned_data.get('htG_tip')
            htG_odds = form.cleaned_data.get('htG_odds')
            htG_result = form.cleaned_data.get('htG_result')

            htH_home_team = form.cleaned_data.get('htH_home_team')
            htH_away_team = form.cleaned_data.get('htH_away_team')
            htH_league = form.cleaned_data.get('htH_league')
            htH_tip = form.cleaned_data.get('htH_tip')
            htH_odds = form.cleaned_data.get('htH_odds')
            htH_result = form.cleaned_data.get('htH_result')

            htI_home_team = form.cleaned_data.get('htI_home_team')
            htI_away_team = form.cleaned_data.get('htI_away_team')
            htI_league = form.cleaned_data.get('htI_league')
            htI_tip = form.cleaned_data.get('htI_tip')
            htI_odds = form.cleaned_data.get('htI_odds')
            htI_result = form.cleaned_data.get('htI_result')


            htJ_home_team = form.cleaned_data.get('htJ_home_team')
            htJ_away_team = form.cleaned_data.get('htJ_away_team')
            htJ_league = form.cleaned_data.get('htJ_league')
            htJ_tip = form.cleaned_data.get('htJ_tip')
            htJ_odds = form.cleaned_data.get('htJ_odds')
            htJ_result = form.cleaned_data.get('htJ_result')

            ## full time

            ftA_home_team = form.cleaned_data.get('ftA_home_team')
            ftA_away_team = form.cleaned_data.get('ftA_away_team')
            ftA_league = form.cleaned_data.get('ftA_league')
            ftA_tip = form.cleaned_data.get('ftA_tip')
            ftA_odds = form.cleaned_data.get('ftA_odds')
            ftA_result = form.cleaned_data.get('ftA_result')

            ftB_home_team = form.cleaned_data.get('ftB_home_team')
            ftB_away_team = form.cleaned_data.get('ftB_away_team')
            ftB_league = form.cleaned_data.get('ftB_league')
            ftB_tip = form.cleaned_data.get('ftB_tip')
            ftB_odds = form.cleaned_data.get('ftB_odds')
            ftB_result = form.cleaned_data.get('ftB_result')

            ftC_home_team = form.cleaned_data.get('ftC_home_team')
            ftC_away_team = form.cleaned_data.get('ftC_away_team')
            ftC_league = form.cleaned_data.get('ftC_league')
            ftC_tip = form.cleaned_data.get('ftC_tip')
            ftC_odds = form.cleaned_data.get('ftC_odds')
            ftC_result = form.cleaned_data.get('ftC_result')

            ftD_home_team = form.cleaned_data.get('ftD_home_team')
            ftD_away_team = form.cleaned_data.get('ftD_away_team')
            ftD_league = form.cleaned_data.get('ftD_league')
            ftD_tip = form.cleaned_data.get('ftD_tip')
            ftD_odds = form.cleaned_data.get('ftD_odds')
            ftD_result = form.cleaned_data.get('ftD_result')

            ftE_home_team = form.cleaned_data.get('ftE_home_team')
            ftE_away_team = form.cleaned_data.get('ftE_away_team')
            ftE_league = form.cleaned_data.get('ftE_league')
            ftE_tip = form.cleaned_data.get('ftE_tip')
            ftE_odds = form.cleaned_data.get('ftE_odds')
            ftE_result = form.cleaned_data.get('ftE_result')

            ftF_home_team = form.cleaned_data.get('ftF_home_team')
            ftF_away_team = form.cleaned_data.get('ftF_away_team')
            ftF_league = form.cleaned_data.get('ftF_league')
            ftF_tip = form.cleaned_data.get('ftF_tip')
            ftF_odds = form.cleaned_data.get('ftF_odds')
            ftF_result = form.cleaned_data.get('ftF_result')

            ftG_home_team = form.cleaned_data.get('ftG_home_team')
            ftG_away_team = form.cleaned_data.get('ftG_away_team')
            ftG_league = form.cleaned_data.get('ftG_league')
            ftG_tip = form.cleaned_data.get('ftG_tip')
            ftG_odds = form.cleaned_data.get('ftG_odds')
            ftG_result = form.cleaned_data.get('ftG_result')

            ftH_home_team = form.cleaned_data.get('ftH_home_team')
            ftH_away_team = form.cleaned_data.get('ftH_away_team')
            ftH_league = form.cleaned_data.get('ftH_league')
            ftH_tip = form.cleaned_data.get('ftH_tip')
            ftH_odds = form.cleaned_data.get('ftH_odds')
            ftH_result = form.cleaned_data.get('ftH_result')

            ftI_home_team = form.cleaned_data.get('ftI_home_team')
            ftI_away_team = form.cleaned_data.get('ftI_away_team')
            ftI_league = form.cleaned_data.get('ftI_league')
            ftI_tip = form.cleaned_data.get('ftI_tip')
            ftI_odds = form.cleaned_data.get('ftI_odds')
            ftI_result = form.cleaned_data.get('ftI_result')


            ftJ_home_team = form.cleaned_data.get('ftJ_home_team')
            ftJ_away_team = form.cleaned_data.get('ftJ_away_team')
            ftJ_league = form.cleaned_data.get('ftJ_league')
            ftJ_tip = form.cleaned_data.get('ftJ_tip')
            ftJ_odds = form.cleaned_data.get('ftJ_odds')
            ftJ_result = form.cleaned_data.get('ftJ_result')
            try:
                data = VipGames.objects.get(id=game_id)
                data.home_team = home_team
                data.away_team = away_team
                data.league = league
                data.tip = tip
                data.odds = odds
                data.result = result

                data.a_home_team = a_home_team
                data.a_away_team = a_away_team
                data.a_league = a_league
                data.a_tip = a_tip
                data.a_odds = a_odds
                data.a_result = a_result

                data.b_home_team = b_home_team
                data.b_away_team = b_away_team
                data.b_league = b_league
                data.b_tip = b_tip
                data.b_odds = b_odds
                data.b_result = b_result

                data.c_home_team = c_home_team
                data.c_away_team = c_away_team
                data.c_league = c_league
                data.c_tip = c_tip
                data.c_odds = c_odds
                data.c_result = c_result

                data.d_home_team = d_home_team
                data.d_away_team = d_away_team
                data.d_league = d_league
                data.d_tip = d_tip
                data.d_odds = d_odds
                data.d_result = d_result


                ## double predictions
                data.dA_home_team = dA_home_team
                data.dA_away_team = dA_away_team
                data.dA_league = dA_league
                data.dA_tip = dA_tip
                data.dA_odds = dA_odds
                data.dA_result = dA_result

                data.dB_home_team = dB_home_team
                data.dB_away_team = dB_away_team
                data.dB_league = dB_league
                data.dB_tip = dB_tip
                data.dB_odds = dB_odds
                data.dB_result = dB_result

                ## multiple prediction 1/3

                data.tA_home_team = tA_home_team
                data.tA_away_team = tA_away_team
                data.tA_league = tA_league
                data.tA_tip = tA_tip
                data.tA_odds = tA_odds
                data.tA_result = tA_result

                data.tB_home_team = tB_home_team
                data.tB_away_team = tB_away_team
                data.tB_league = tB_league
                data.tB_tip = tB_tip
                data.tB_odds = tB_odds
                data.tB_result = tB_result

                data.tC_home_team = tC_home_team
                data.tC_away_team = tC_away_team
                data.tC_league = tC_league
                data.tC_tip = tC_tip
                data.tC_odds = tC_odds
                data.tC_result = tC_result

                ## multiple prediction 1/4

                data.fA_home_team = fA_home_team
                data.fA_away_team = fA_away_team
                data.fA_league = fA_league
                data.fA_tip = fA_tip
                data.fA_odds = fA_odds
                data.fA_result = fA_result

                data.fB_home_team = fB_home_team
                data.fB_away_team = fB_away_team
                data.fB_league = fB_league
                data.fB_tip = fB_tip
                data.fB_odds = fB_odds
                data.fB_result = fB_result

                data.fC_home_team = fC_home_team
                data.fC_away_team = fC_away_team
                data.fC_league = fC_league
                data.fC_tip = fC_tip
                data.fC_odds = fC_odds
                data.fC_result = fC_result

                data.fD_home_team = fD_home_team
                data.fD_away_team = fD_away_team
                data.fD_league = fD_league
                data.fD_tip = fD_tip
                data.fD_odds = fD_odds
                data.fD_result = fD_result

                ## multiple prediction 1/5

                data.ffA_home_team = ffA_home_team
                data.ffA_away_team = ffA_away_team
                data.ffA_league = ffA_league
                data.ffA_tip = ffA_tip
                data.ffA_odds = ffA_odds
                data.ffA_result = ffA_result

                data.ffB_home_team = ffB_home_team
                data.ffB_away_team = ffB_away_team
                data.ffB_league = ffB_league
                data.ffB_tip = ffB_tip
                data.ffB_odds = ffB_odds
                data.ffB_result = ffB_result

                data.ffC_home_team = ffC_home_team
                data.ffC_away_team = ffC_away_team
                data.ffC_league = ffC_league
                data.ffC_tip = ffC_tip
                data.ffC_odds = ffC_odds
                data.ffC_result = ffC_result

                data.ffD_home_team = ffD_home_team
                data.ffD_away_team = ffD_away_team
                data.ffD_league = ffD_league
                data.ffD_tip = ffD_tip
                data.ffD_odds = ffD_odds
                data.ffD_result = ffD_result

                data.ffE_home_team = ffE_home_team
                data.ffE_away_team = ffE_away_team
                data.ffE_league = ffE_league
                data.ffE_tip = ffE_tip
                data.ffE_odds = ffE_odds
                data.ffE_result = ffE_result

                ## multiple prediction 1/6

                data.siA_home_team = siA_home_team
                data.siA_away_team = siA_away_team
                data.siA_league = siA_league
                data.siA_tip = siA_tip
                data.siA_odds = siA_odds
                data.siA_result = siA_result

                data.siB_home_team = siB_home_team
                data.siB_away_team = siB_away_team
                data.siB_league = siB_league
                data.siB_tip = siB_tip
                data.siB_odds = siB_odds
                data.siB_result = siB_result

                data.siC_home_team = siC_home_team
                data.siC_away_team = siC_away_team
                data.siC_league = siC_league
                data.siC_tip = siC_tip
                data.siC_odds = siC_odds
                data.siC_result = siC_result

                data.siD_home_team = siD_home_team
                data.siD_away_team = siD_away_team
                data.siD_league = siD_league
                data.siD_tip = siD_tip
                data.siD_odds = siD_odds
                data.siD_result = siD_result

                data.siE_home_team = siE_home_team
                data.siE_away_team = siE_away_team
                data.siE_league = siE_league
                data.siE_tip = siE_tip
                data.siE_odds = siE_odds
                data.siE_result = siE_result

                data.siF_home_team = siF_home_team
                data.siF_away_team = siF_away_team
                data.siF_league = siF_league
                data.siF_tip = siF_tip
                data.siF_odds = siF_odds
                data.siF_result = siF_result

                ## multiple prediction 1/7

                data.sA_home_team = sA_home_team
                data.sA_away_team = sA_away_team
                data.sA_league = sA_league
                data.sA_tip = sA_tip
                data.sA_odds = sA_odds
                data.sA_result = sA_result

                data.sB_home_team = sB_home_team
                data.sB_away_team = sB_away_team
                data.sB_league = sB_league
                data.sB_tip = sB_tip
                data.sB_odds = sB_odds
                data.sB_result = sB_result

                data.sC_home_team = sC_home_team
                data.sC_away_team = sC_away_team
                data.sC_league = sC_league
                data.sC_tip = sC_tip
                data.sC_odds = sC_odds
                data.sC_result = sC_result

                data.sD_home_team = sD_home_team
                data.sD_away_team = sD_away_team
                data.sD_league = sD_league
                data.sD_tip = sD_tip
                data.sD_odds = sD_odds
                data.sD_result = sD_result

                data.sE_home_team = sE_home_team
                data.sE_away_team = sE_away_team
                data.sE_league = sE_league
                data.sE_tip = sE_tip
                data.sE_odds = sE_odds
                data.SE_result = SE_result

                data.sF_home_team = sF_home_team
                data.sF_away_team = sF_away_team
                data.sF_league = sF_league
                data.sF_tip = sF_tip
                data.sF_odds = sF_odds
                data.sF_result = sF_result

                data.gF_home_team = gF_home_team
                data.gF_away_team = gF_away_team
                data.gF_league = gF_league
                data.gF_tip = gF_tip
                data.gF_odds = gF_odds
                data.gF_result = gF_result

                ## both teams to score (gg)

                data.ggA_home_team = ggA_home_team
                data.ggA_away_team = ggA_away_team
                data.ggA_league = ggA_league
                data.ggA_tip = ggA_tip
                data.ggA_odds = ggA_odds
                data.ggA_result = ggA_result

                data.ggB_home_team = ggB_home_team
                data.ggB_away_team = ggB_away_team
                data.ggB_league = ggB_league
                data.ggB_tip = ggB_tip
                data.ggB_odds = ggB_odds
                data.ggB_result = ggB_result

                data.ggC_home_team = ggC_home_team
                data.ggC_away_team = ggC_away_team
                data.ggC_league = ggC_league
                data.ggC_tip = ggC_tip
                data.ggC_odds = ggC_odds
                data.ggC_result = ggC_result

                data.ggD_home_team = ggD_home_team
                data.ggD_away_team = ggD_away_team
                data.ggD_league = ggD_league
                data.ggD_tip = ggD_tip
                data.ggD_odds = ggD_odds
                data.ggD_result = ggD_result

                data.ggE_home_team = ggE_home_team
                data.ggE_away_team = ggE_away_team
                data.ggE_league = ggE_league
                data.ggE_tip = ggE_tip
                data.ggE_odds = ggE_odds
                data.ggE_result = ggE_result

                data.ggF_home_team = ggF_home_team
                data.ggF_away_team = ggF_away_team
                data.ggF_league = ggF_league
                data.ggF_tip = ggF_tip
                data.ggF_odds = ggF_odds
                data.ggFresult = ggFresult

                data.ggG_home_team = ggG_home_team
                data.ggG_away_team = ggG_away_team
                data.ggG_league = ggG_league
                data.ggG_tip = ggG_tip
                data.ggG_odds = ggG_odds
                data.ggG_result = ggG_result

                data.ggH_home_team = ggH_home_team
                data.ggH_away_team = ggH_away_team
                data.ggH_league = ggH_league
                data.ggH_tip = ggH_tip
                data.ggH_odds = ggH_odds
                data.ggH_result = ggH_result

                data.ggI_home_team = ggI_home_team
                data.ggI_away_team = ggI_away_team
                data.ggI_league = ggI_league
                data.ggI_tip = ggI_tip
                data.ggI_odds = ggI_odds
                data.ggI_result = ggI_result

                data.ggJ_home_team = ggJ_home_team
                data.ggJ_away_team = ggJ_away_team
                data.ggJ_league = ggJ_league
                data.ggJ_tip = ggJ_tip
                data.ggJ_odds = ggJ_odds
                data.ggJ_result = ggJ_result

                ## correct score (cc)

                data.ccA_home_team = ccA_home_team
                data.ccA_away_team = ccA_away_team
                data.ccA_league = ccA_league
                data.ccA_tip = ccA_tip
                data.ccA_odds = ccA_odds
                data.ccA_result = ccA_result

                data.ccB_home_team = ccB_home_team
                data.ccB_away_team = ccB_away_team
                data.ccB_league = ccB_league
                data.ccB_tip = ccB_tip
                data.ccB_odds = ccB_odds
                data.ccB_result = ccB_result

                data.ccC_home_team = ccC_home_team
                data.ccC_away_team = ccC_away_team
                data.ccC_league = ccC_league
                data.ccC_tip = ccC_tip
                data.ccC_odds = ccC_odds
                data.ccC_result = ccC_result

                data.ccD_home_team = ccD_home_team
                data.ccD_away_team = ccD_away_team
                data.ccD_league = ccD_league
                data.ccD_tip = ccD_tip
                data.ccD_odds = ccD_odds
                data.ccD_result = ccD_result

                data.ccE_home_team = ccE_home_team
                data.ccE_away_team = ccE_away_team
                data.ccE_league = ccE_league
                data.ccE_tip = ccE_tip
                data.ccE_odds = ccE_odds
                data.ccE_result = ccE_result

                data.ccF_home_team = ccF_home_team
                data.ccF_away_team = ccF_away_team
                data.ccF_league = ccF_league
                data.ccF_tip = ccF_tip
                data.ccF_odds = ccF_odds
                data.ccF_result = ccF_result

                data.ccG_home_team = ccG_home_team
                data.ccG_away_team = ccG_away_team
                data.ccG_league = ccG_league
                data.ccG_tip = ccG_tip
                data.ccG_odds = ccG_odds
                data.ccG_result = ccG_result

                data.ccH_home_team = ccH_home_team
                data.ccH_away_team = ccH_away_team
                data.ccH_league = ccH_league
                data.ccH_tip = ccH_tip
                data.ccH_odds = ccH_odds
                data.ccH_result = ccH_result

                data.ccI_home_team = ccI_home_team
                data.ccI_away_team = ccI_away_team
                data.ccI_league = ccI_league
                data.ccI_tip = ccI_tip
                data.ccI_odds = ccI_odds
                data.ccI_result = ccI_result

                data.ccJ_home_team = ccJ_home_team
                data.ccJ_away_team = ccJ_away_team
                data.ccJ_league = ccJ_league
                data.ccJ_tip = ccJ_tip
                data.ccJ_odds = ccJ_odds
                data.ccJ_result = ccJ_result

                ## half-time score (ht)

                data.htA_home_team = htA_home_team
                data.htA_away_team = htA_away_team
                data.htA_league = htA_league
                data.htA_tip = htA_tip
                data.htA_odds = htA_odds
                data.htA_result = htA_result

                data.htB_home_team = htB_home_team
                data.htB_away_team = htB_away_team
                data.htB_league = htB_league
                data.htB_tip = htB_tip
                data.htB_odds = htB_odds
                data.htB_result = htB_result

                data.htC_home_team = htC_home_team
                data.htC_away_team = htC_away_team
                data.htC_league = htC_league
                data.htC_tip = htC_tip
                data.htC_odds = htC_odds
                data.htC_result = htC_result

                data.htD_home_team = htD_home_team
                data.htD_away_team = htD_away_team
                data.htD_league = htD_league
                data.htD_tip = htD_tip
                data.htD_odds = htD_odds
                data.htD_result = htD_result

                data.htE_home_team = htE_home_team
                data.htE_away_team = htE_away_team
                data.htE_league = htE_league
                data.htE_tip = htE_tip
                data.htE_odds = htE_odds
                data.htE_result = htE_result

                data.htF_home_team = htF_home_team
                data.htF_away_team = htF_away_team
                data.htF_league = htF_league
                data.htF_tip = htF_tip
                data.htF_odds = htF_odds
                data.htF_result = htF_result

                data.htG_home_team = htG_home_team
                data.htG_away_team = htG_away_team
                data.htG_league = htG_league
                data.htG_tip = htG_tip
                data.htG_odds = htG_odds
                data.htG_result = htG_result

                data.htH_home_team = htH_home_team
                data.htH_away_team = htH_away_team
                data.htH_league = htH_league
                data.htH_tip = htH_tip
                data.htH_odds = htH_odds
                data.htH_result = htH_result

                data.htI_home_team = htI_home_team
                data.htI_away_team = htI_away_team
                data.htI_league = htI_league
                data.htI_tip = htI_tip
                data.htI_odds = htI_odds
                data.htI_result = htI_result

                data.htJ_home_team = htJ_home_team
                data.htJ_away_team = htJ_away_team
                data.htJ_league = htJ_league
                data.htJ_tip = htJ_tip
                data.htJ_odds = htJ_odds
                data.htJ_result = htJ_result


                ## full-time score (ft)

                data.ftA_home_team = ftA_home_team
                data.ftA_away_team = ftA_away_team
                data.ftA_league = ftA_league
                data.ftA_tip = ftA_tip
                data.ftA_odds = ftA_odds
                data.ftA_result = ftA_result

                data.ftB_home_team = ftB_home_team
                data.ftB_away_team = ftB_away_team
                data.ftB_league = ftB_league
                data.ftB_tip = ftB_tip
                data.ftB_odds = ftB_odds
                data.ftB_result = ftB_result

                data.ftC_home_team = ftC_home_team
                data.ftC_away_team = ftC_away_team
                data.ftC_league = ftC_league
                data.ftC_tip = ftC_tip
                data.ftC_odds = ftC_odds
                data.ftC_result = ftC_result

                data.ftD_home_team = ftD_home_team
                data.ftD_away_team = ftD_away_team
                data.ftD_league = ftD_league
                data.ftD_tip = ftD_tip
                data.ftD_odds = ftD_odds
                data.ftD_result = ftD_result

                data.ftE_home_team = ftE_home_team
                data.ftE_away_team = ftE_away_team
                data.ftE_league = ftE_league
                data.ftE_tip = ftE_tip
                data.ftE_odds = ftE_odds
                data.ftE_result = ftE_result

                data.ftF_home_team = ftF_home_team
                data.ftF_away_team = ftF_away_team
                data.ftF_league = ftF_league
                data.ftF_tip = ftF_tip
                data.ftF_odds = ftF_odds
                data.ftF_result = ftF_result

                data.ftG_home_team = ftG_home_team
                data.ftG_away_team = ftG_away_team
                data.ftG_league = ftG_league
                data.ftG_tip = ftG_tip
                data.ftG_odds = ftG_odds
                data.ftG_result = ftG_result

                data.ftH_home_team = ftH_home_team
                data.ftH_away_team = ftH_away_team
                data.ftH_league = ftH_league
                data.ftH_tip = ftH_tip
                data.ftH_odds = ftH_odds
                data.ftH_result = ftH_result

                data.ftI_home_team = ftI_home_team
                data.ftI_away_team = ftI_away_team
                data.ftI_league = ftI_league
                data.ftI_tip = ftI_tip
                data.ftI_odds = ftI_odds
                data.ftI_result = ftI_result

                data.ftJ_home_team = ftJ_home_team
                data.ftJ_away_team = ftJ_away_team
                data.ftJ_league = ftJ_league
                data.ftJ_tip = ftJ_tip
                data.ftJ_odds = ftJ_odds
                data.ftJ_result = ftJ_result
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
