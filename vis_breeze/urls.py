from django.urls import path
from .views import index, about, contact


app_name = 'vis_breeze'

urlpatterns = [
  
    path('', index, name='index'),
    path('about/', about, name='about_us'),
    path('contact/', contact, name='contact_us'),
    # path('login_cnd', loginCnd, name='login_cnd'),
    # path('about_cnd', about, name='about_cnd'),

    
    
]