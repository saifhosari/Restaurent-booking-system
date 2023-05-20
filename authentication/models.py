from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    confirm_password = models.TextField(max_length=500, blank=True)


class Table(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    table = models.IntegerField(max_length=3,  default=0, null=True)
    
    