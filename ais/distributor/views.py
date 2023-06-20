from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'distributor/home.html')

def sign_up(request):
    return render(request, 'distributor/signup.html')

def log_in(request):
    return render(request, 'distributor/login.html')

def req(request):
    return render(request, 'distributor/request.html')