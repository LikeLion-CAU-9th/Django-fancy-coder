from django.urls import path
from .views import *

app_name = "reservation"

urlpatterns = [
    path('create/<int:pk>', reservation_create, name="reservation_create"),
    path('success/', reservation_success, name="reservation_success"),
    path('payment/<int:pk>', reservation_pay_method, name="reservation_pay_method"),

    #TODO AJAX 구현 후 연결해야 함
    #Profile 즉 Service Provider 가 모든 예약 정보를 확인하는 페이지
    path('all/<int:pk>', reservation_host_confirm, name="reservation_host_confirm"),
    #Customer가 자신이 예약한 정보를 확인하는 페이지
    path('confirm/', reservation_customer_confirm, name="reservation_customer_confirm"),
]

