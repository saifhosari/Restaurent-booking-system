from django.contrib import admin
from authentication.models import Table, Booking, Profile, Guest
from django.contrib.admin.models import LogEntry

# Register your models here.
@admin.register(Table)
class addTable(admin.ModelAdmin):
    list_display = ["table_name", "profile_username"]

    def profile_username(self, obj):
        return obj.profile.username

    profile_username.short_description = "Profile Username"



@admin.register(Guest)
class addGuest(admin.ModelAdmin):
    list_display = ["guest_name", "guest_phone", "created_at"]
    


class addBooking(admin.ModelAdmin):
    list_display = ["from_time", "to_time", "check_in", "registered_with_username"]

    def registered_with_username(self, obj):
        return obj.registered_with.username
    
    def get_change_message(self, request, obj):
        if obj is None:
            return f"{obj.registered_with.username} Booked a reservation"
        else:
            return 'Delete Booking'

    registered_with_username.short_description = "Registered with"

@admin.register(Profile)
class addProfile(admin.ModelAdmin):
    list_display = ["user_username", "user_email", "user_is_superuser"]

    def user_username(self, obj):
        return obj.user.username

    def user_email(self, obj):
        return obj.user.email

    def user_is_superuser(self, obj):
        return obj.user.is_superuser

    user_username.short_description = "Name"
    user_email.short_description = "Email Address"
    user_is_superuser.short_description = "Is Super User"

admin.site.register(Booking, addBooking)
