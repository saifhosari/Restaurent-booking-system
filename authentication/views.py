from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .models import Profile

def register(request):
    context = {}
    if request.method == 'POST':
        print(request.POST)
        try:
            print("=== in try ===")
            user_name = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            confirm_password = request.POST.get('confirm_password')
            print("user_name", user_name)
            print("Password:", password)
            print("Email", email)
            print("Confirm Password", confirm_password)
            print(" == after confirm password ===")
            user_exists = User.objects.get(username=user_name)
            print(user_exists)
            if user_exists:
                context['developer_msg'] = f'User name {user_exists.username} already exists'
            elif password == confirm_password:
                user_obj = User.objects.create_user(username=user_name, email=email, password=password)
                user_profile = Profile.objects.create(user=user_obj, confirm_password=confirm_password)
                user_profile.save()
                context['developer_msg'] = 'Successfully Registered'
            else:
                context['developer_msg'] = 'Your Password does not match'
                return JsonResponse(context)
        except Exception as e:
            print("Exception#", e)
            context['developer_msg'] = 'Something went wrong'

    return JsonResponse(context)

def login_user(request):
    print("--- in login user----")
    print("POST REQUEST", request.POST)
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            login_user = authenticate(request=request, username=username, password=password)
            context['developer_msg'] = f'{login_user.username} successfully logged in.'
            return JsonResponse(context)
        except Exception as e:
            print("Exception #", e)
            context['developer_msg'] = f'User with {username} does not exists.'
            return JsonResponse(context)

    return JsonResponse(context)