from django.urls import path


from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("contact/", views.contact, name='contact'),
    path("about/", views.about, name='about'),
    path("faq/", views.faq, name='faq'),
    path("predict/", views.predict, name='predict'),
    path("vip_game/", views.vip_game, name='vip_game'),
    path("subscribe/", views.subscribe, name='subscribe'),
    path("signup/", views.signup, name='signup'),
    path("signin/", views.signin, name='signin'),
    path('logout/', views.logout_func, name='logout_form'),
    path("livescores/", views.livescores, name='livescores'),
    path("policy/", views.policy, name='policy'),

    ###admin dashboard
    path("boss/", views.boss, name='boss'),
    ###admin upload games
    path("games/", views.games, name='games'),
    path("manage_games/", views.manage_games, name='manage_games'),
    path("game/edit/<int:game_id>", views.edit_game, name='edit_game'),
     path("game/delete/<int:id>", views.delete_game, name='delete_game'),

    ###admin upload ads
    path("ads/", views.ads, name='ads'),
    path("manage_advert/", views.manage_advert, name='manage_advert'),
    path("advert/edit/<int:pk>", views.edit_advert, name='edit_advert'),
    path("advert/delete/<int:id>", views.delete_advert, name='delete_advert'),
    
    ### admin recieve contact mssg
    path("contact_message/", views.contact_message, name='contact_message'),

    path("message/", views.message, name='message'),
    path("manage_message/", views.manage_message, name='manage_message'),
    path("message/edit/<int:message_id>", views.edit_message, name='edit_message'),
    path("message/delete/<int:id>", views.delete_message, name='delete_message'),
]
