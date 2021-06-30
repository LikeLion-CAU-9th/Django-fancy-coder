from django import forms
from .models import *

#TODO calander https://stackoverflow.com/questions/5449604/django-calendar-widget-in-a-custom-form

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ["customer_count", "activate_date"]

class ReservationPaymentForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ["payment_method"]
