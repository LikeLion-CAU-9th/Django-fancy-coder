from django.contrib import admin
from django.urls import path
import accounts.views


urlpatterns = [
    path('', accounts.views.index, name="index"),
    path('signup/check', accounts.views.signup_main, name="signup_main"),
    path('signup/information', accounts.views.signup_infor, name="signup_infor"),
    
]

