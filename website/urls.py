from django.contrib import admin
from django.urls import path
from website.views import *

app_name = 'website'

urlpatterns = [
    path('', index, name= 'index'),
    path('about', about, name= 'about'),
    path('contact', contact, name= 'contact'),
    path('resume', resume, name= 'resume'),

]
