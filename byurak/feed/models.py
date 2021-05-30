from django.db import models
from uuid import uuid4
from datetime import datetime
from django.utils import timezone
import os

def uuid_name_upload_to(instance, filename):
    ymd_path = datetime.now().strftime('%Y/%m/%d')  # 업로드하는 년/월/일 별로
    uuid_name = uuid4().hex
    extension = os.path.splitext(filename)[-1].lower()  # 확장자 추출하고, 소문자로 변환
    return '/'.join([
        ymd_path,
        uuid_name[:2],
        uuid_name + extension,
    ])

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to=uuid_name_upload_to, blank=True, null=True)
    body=models.TextField(help_text="본문을 입력하세요")
    date_time=models.DateTimeField(default=timezone.now)
    created_at=models.DateField(auto_now_add=True)