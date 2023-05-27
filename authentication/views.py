from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Profile
from django.shortcuts import redirect, render



# Register_user
def register(request):
    context = {}
    if request.method == 'POST':
        print("I am here")
    try:
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        confirm_password = request.POST.get('confirm_password')
        try:

            user_exists = User.objects.get(username=user_name)
           
            if user_exists:
                context['developer_msg'] = f'User name {user_exists.username} already exists'
                response = 1
        except User.DoesNotExist:
            
            if password == confirm_password:
                # user_obj = User.objects.create(username=user_name, email=email, password=password)
                new_user, created = User.objects.get_or_create(username=user_name, is_staff=True, email=email)
                new_user.set_password(password)
                new_user.save()
                # user_obj.save()
                user_profile = Profile.objects.create(user=new_user, confirm_password=confirm_password)
                user_profile.save()
                context['developer_msg'] = 'Successfully Registered'
                response = 2
            else:
                context['developer_msg'] = 'Your Password does not match'
                response = 3
        context['response'] = response
        # return JsonResponse(context)
    except Exception as e:
        print("Exception#", e)
        context['developer_msg'] = 'Something went wrong'

    return JsonResponse(context)


# login user
def login_user(request):
    context = {}
    response = 0
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            login_user_obj = User.objects.get(username=username)
            login_user_obj = authenticate(request=request, username=username, password=password)
            if login_user_obj is not None:
                login(request, login_user_obj)
                context['username'] = login_user_obj.username
                context['developer_msg'] = f'{login_user_obj.username} successfully logged in.'
                context['response'] = 1
                response = 1
                return JsonResponse(context)
            
        except User.DoesNotExist as e:
            print("Exception #", e)
            context['developer_msg'] = f'User with {username} does not exists.'
            response = 2
    context['response'] = response
            # return JsonResponse(context)
    return JsonResponse(context)


# Logout user
def logout_user(request):
    logout(request)
    return redirect('home_page')
