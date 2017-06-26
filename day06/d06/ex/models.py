from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class MyUser(AbstractUser):
   name = models.CharField(max_length=64, null=False, unique=True)
   password = models.CharField(max_length=255, null=False, unique=False)



