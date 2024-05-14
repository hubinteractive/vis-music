from django.urls import path
from .views import index, about, contact, lana_janjanin, jazz_orchestra, kafka, vlatko, dilatum, matija, vasil, programme, terms, subscribe, success, pdf


app_name = 'vis_breeze'

urlpatterns = [
  
    path('', index, name='index'),
    path('about/', about, name='about_us'),
    path('contact/', contact, name='contact_us'),
    path('success/', success, name='success'),
    path('lana_janjanin/', lana_janjanin, name='lana_janjanin'),
    path('jazz_orchestra/', jazz_orchestra, name='jazz_orchestra'),
    path('kafka/', kafka, name='kafka'),
    path('vlatko/', vlatko, name='vlatko'),
    path('dilatum/', dilatum, name='dilatum'),
    path('matija/', matija, name='matija'),
    path('vasil/', vasil, name='vasil'), 
    path('programme/', programme, name='programme'), 
    path('terms/', terms, name='terms'), 
    path('subscribe/', subscribe, name='subscribe'), 
    path('pdf/', pdf, name='pdf'), 
    # path('login_cnd', loginCnd, name='login_cnd'),
    # path('about_cnd', about, name='about_cnd'),

    
    
]