from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'home/index.html')

def about(request):
    # Your about view code here
    return render(request, 'home/about.html')

def contact(request):
    # Your contact view code here
    return render(request, 'home/contact.html')

