from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'index.html')


def contact_us(request):
    return render(request, 'contact.html')
