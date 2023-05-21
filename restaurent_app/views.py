from django.shortcuts import render
from authentication.models import *
from datetime import datetime
import json


# Create your views here.
def home_page(request):
    template = 'index.html'
    return render(request, template)


def contact_us(request):
    template = 'contact.html'
    return render(request, template)


def book_table(request):
    template = 'booking.html'

    if request.method == 'POST':
        user = User.objects.get(username="talha")
        reservation_user = request.POST.get('reservation_user')
        table_name = request.POST.get('table_name')
        email = request.POST.get('email')
        check_in = request.POST.get('check_in')
        time_in = datetime.strptime(request.POST.get('time_in'), '%I:%M %p')
        time_out = datetime.strptime(request.POST.get('time_out'), '%I:%M %p')
        special_req = request.POST.get('special_request')

    try:
        guest_cnic = json.loads(request.POST.get('guest_cnic'))
        guest_names = json.loads(request.POST.get('guest_names'))
        guest_list = [{name: cnic} for name, cnic in zip(guest_names, guest_cnic)]
        guests = []
        if guest_cnic != [] and guest_names !=[]:
            for name, cnic in guest_list[0].items():
                guests.append(Guest.objects.create(guest_name=name, guest_cnic=cnic))

        table_obj = Table.objects.create(profile=user, table_name=table_name)
        table_obj.save()
        table_obj.guests.add(*guests)
        book_table = Booking.objects.create(from_time=time_in, to_time=time_out, registered_with=user)
        book_table.save()
        book_table.table.add(table_obj)

    except Exception as e:
            print("Exception #", e)


        
        
    return render(request, template)
