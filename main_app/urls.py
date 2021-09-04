from django.urls import path


from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("contact/", views.contact, name='contact'),
    path("about/", views.about, name='about'),
    path("faq/", views.faq, name='faq'),
    path("predict/", views.predict, name='predict'),
    path("vip/", views.vip, name='vip'),
    path("subscribe/", views.subscribe, name='subscribe'),
    path("signup/", views.signup, name='signup'),
    path("signin/", views.signin, name='signin'),
    path("livescores/", views.livescores, name='livescores'),
    path("policy/", views.policy, name='policy'),
]
