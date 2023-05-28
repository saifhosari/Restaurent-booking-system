from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    confirm_password = models.TextField(max_length=500, blank=True)


class Guest(models.Model):
    guest_name = models.CharField(max_length=20, null=True, blank=True)
    guest_phone = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.guest_name
    

class Table(models.Model):
    table_name = models.CharField(max_length=30, default="default_tables1")
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    guests = models.ManyToManyField(Guest)


class Booking(models.Model):
    table = models.ManyToManyField(Table)
    name = models.TextField(null=True)
    registered_with = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    from_time = models.DateTimeField(default=datetime.datetime.now())
    to_time = models.DateTimeField(default=datetime.datetime.now())
    check_in = models.DateTimeField(default=datetime.datetime.now())
    special_request = models.TextField(max_length=400, default="Nothing to Add Special")