
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('booking/', views.book_table, name='booking'),
    # path('bookings-list/', views.get_all_booking_list, name='booking_list'),
    path('bookings/', views.bookings, name='bookings'),
    path('bookings/delete/<int:pk>', views.delete_booking, name="delete_bookings"),
    path('about/', views.about_us, name='about_us'),
]