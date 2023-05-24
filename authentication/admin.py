from django.contrib import admin
from authentication.models import *
# Register your models here.
@admin.register(Table)
class addTable(admin.ModelAdmin):
    list_display = ["table_name", "profile_username"]

    def profile_username(self, obj):
        return obj.profile.username

    profile_username.short_description = "Profile Username"

admin.site.register(Booking)
admin.site.register(Profile)
admin.site.register(Guest)