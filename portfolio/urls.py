from django.contrib import admin
from django.urls import path
from portfolio.views import *

urlpatterns = [
    path('', portfolio),
    path('portfolio/portfolio-details', portfolio_details),
]
