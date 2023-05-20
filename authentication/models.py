from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    confirm_password = models.TextField(max_length=500, blank=True)


class Guest(models.Model):
    guest_name = models.CharField(max_length=20, null=True, blank=True)
    guest_cnic = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.guest_name
    
class Table(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    table = models.ManyToManyField(Guest)


class Booking(models.Model):
    table = models.ManyToManyField(Table)
    registered_with = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
