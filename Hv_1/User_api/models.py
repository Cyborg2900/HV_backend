from django.db import models
import uuid

# Create your models here.
class UserData(models.Model):
    UserName=models.CharField(max_length=30,default='')
    UserId=models.UUIDField(default=uuid.uuid4)
    name=models.CharField(max_length=30,default='')
    email=models.CharField(max_length=30,default='')
    password=models.CharField(max_length=15,default='')
    