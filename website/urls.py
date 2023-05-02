from django.contrib import admin
from django.urls import path
from website.views import *

urlpatterns = [
    path('', index),
    path('about', about),
    path('contact', contact),
    path('resume', resume),
    path('services', services),
]
