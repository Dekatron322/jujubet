from django.contrib import admin
from main_app.models import UserProfile, Message, Advert, VipGames

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ['user_name', 'address', 'phone', 'city',]

admin.site.register(UserProfile, UserProfileAdmin)

admin.site.register(Message)

admin.site.register(Advert)

admin.site.register(VipGames)