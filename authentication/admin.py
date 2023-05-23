from django.contrib import admin
from authentication.models import *
# Register your models here.

admin.site.register(Table)
admin.site.register(Booking)
admin.site.register(Profile)
admin.site.register(Guest)