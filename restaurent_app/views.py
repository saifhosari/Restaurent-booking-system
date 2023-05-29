from django.shortcuts import render,redirect
from django.http import JsonResponse
from authentication.models import Table, Guest, Booking
from django.contrib.auth.models import User
from datetime import datetime
import json


# Create your views here.
def home_page(request):
    template = 'index.html'
    return render(request, template)


def contact_us(request):
    template = 'contact.html'
    return render(request, template)


def about_us(request):
    template = 'about.html'
    return render(request, template)


def book_table(request):
    template = 'booking.html'
    context = {}

    if request.method == 'POST':
        try:
            user = User.objects.get(username=request.user.username)
            name = request.POST.get('reservation_user')
            table_name = request.POST.get('table_name')
            check_in = request.POST.get('check_in')
            time_in = datetime.strptime(request.POST.get('time_in'), '%I:%M %p')
            time_out = datetime.strptime(request.POST.get('time_out'), '%I:%M %p')
            special_req = request.POST.get('special_request')
            # tables = Table.objects.filter(profile=user, table_name=table_name)
            # print(tables)
            
            try:
                guest_phone = json.loads(request.POST.get('guest_phone'))
                guest_names = json.loads(request.POST.get('guest_names'))
                guest_list = [{name: cnic} for name, cnic in zip(guest_names, guest_phone)]
                guests = []
                if guest_phone != [] and guest_names !=[]:
                    for name, phone in guest_list[0].items():
                        guests.append(Guest.objects.create(guest_name=name, guest_phone=phone))

    
                # Check if the user has any tables booked
                if_table_booked = Booking.objects.filter(from_time=time_in, to_time=time_out, check_in=check_in)
                tables_booked = list(Table.objects.filter(booking__in=if_table_booked).values_list('table_name'))

                if any(table_name in name[0] for name in tables_booked):
                    context['developer_msg'] = 'Please choose another table it is already booked by you'
                    return JsonResponse(context)
                
                table_obj = Table.objects.create(profile=user, table_name=table_name)
                table_obj.save()
                table_obj.guests.add(*guests)
                book_table = Booking.objects.create(from_time=time_in, to_time=time_out, registered_with=user, check_in=check_in, name=name)
                book_table.save()
                book_table.table.add(table_obj)

                #Get the guests against the user
                context['reserved_user'] = user.username
                context['no_of_guests'] = len(guests)
                context['guest_names'] = guest_list
                context['check_in'] = check_in
                return JsonResponse(context)
            except Exception as e:    
                return JsonResponse(context)
             
        except Exception as e:
            context['developer_msg'] = 'You are not logged in!'
            return JsonResponse(context)
        
    return render(request, template)


def bookings(request):
    context = {}
    print(request.user)
    user_obj = User.objects.get(username=request.user.username)
    all_bookings = Booking.objects.filter(registered_with=user_obj)
    context['all_bookings'] = all_bookings
    return render(request, 'bookings.html', context)

def delete_booking(request, pk):
    print(pk)
    context = {}
    try:
        booking_obj = Booking.objects.get(id=pk)
        booking_obj.delete()
        context['response'] = 1
    except:
        context['response'] = 2  

    return JsonResponse(context)

