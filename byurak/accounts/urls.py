from django.contrib import admin
from django.urls import path
import accounts.views


urlpatterns = [
    path('', accounts.views.accounts_home, name="accounts_home"),
    path('signup/', accounts.views.accounts_signup, name='accounts_signup'),
    path('login/', accounts.views.accounts_login, name='accounts_login'),
    path('logout/', accounts.views.accounts_logout, name='accounts_logout'),
    path("signup_success/", accounts.views.signup_success, name='signup_success'),
    path("login_success/", accounts.views.login_success, name="login_success"),
    path("logout_success/", accounts.views.logout_success, name="logout_success"),
]

