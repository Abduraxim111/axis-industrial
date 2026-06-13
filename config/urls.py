
from django.contrib import admin
from django.urls import path
from axis.views import home_page,landing_page,the_observer


urlpatterns = [
    path('',home_page, name='index'),
    path('landing-page/', landing_page, name='landing_page'),
    path('the-observer/',the_observer, name='the_observer'), 
]
