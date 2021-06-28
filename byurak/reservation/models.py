from django.db import models

#TODO 개발 끝내고 정리하기
from accounts.models import *

# Create your models here.

PAYMENT_METHOD_CHOICES = (
    ("무통장 입금", "무통장 입금"),
    ("계좌 이체", "계좌 이체"),
)

class Reservation(models.Model):
    service = models.ForeignKey(Profile, related_name = "service_set", on_delete = models.CASCADE, blank=True, null=True)
    customer = models.ForeignKey(User, related_name = "customer_set", on_delete = models.CASCADE, blank=True, null=True)
    customer_count = models.PositiveIntegerField(default = 1)
    activate_date = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    payment_fee = models.PositiveIntegerField(default=0)
    payment_method = models.CharField(max_length = 30, choices=PAYMENT_METHOD_CHOICES, blank=True, null=True)
    is_complete = models.BooleanField(default = False)

    def __str__(self):
        return "%s : %s" % (self.service.user.name, self.customer.name)
    