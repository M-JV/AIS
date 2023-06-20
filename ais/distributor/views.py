from django.shortcuts import render, redirect
from .models import Distributor, TemporaryD, Requests
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request, 'distributor/home.html')

def sign_up(request):
    if request.method == 'GET':
        return render(request, 'distributor/signup.html')
    else:
        # Handle the form submission
        username = request.POST["username"]
        email = request.POST["email"]
        contact = request.POST["contact"]
        password = request.POST["password"]
        password_repeat = request.POST["password_repeat"]
       
        if password == password_repeat:
            if Distributor.objects.filter(distributorName=username).exists():
                messages.info(request, "Username Already Taken")
                return redirect('signup')
            elif Distributor.objects.filter(distributorEmail=email).exists():
                messages.info(request, "Email Already Taken")
                return redirect('signup')
            elif contact == "":
                messages.info(request, "Empty fields")
                return redirect('signup')
            else:
                distributor_info = Distributor(distributorName=username, distributorEmail=email, distributorContact=contact,
                                     distributorPassword=password)
                distributor_info.save()
                return redirect('login')
        else:
            messages.info(request, "Password does not match")
            return redirect('signup')

def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if Distributor.objects.filter(distributorName=username).exists():
            if Distributor.objects.filter(distributorPassword=password).exists():

                distributor = Distributor.objects.get(Q(distributorName=username) & Q(distributorPassword=password))

                temporary_info = TemporaryD(id=1, distributorName=username, distributorPassword=password)
                temporary_info.save()

                context = {"distributor": distributor}
                return render(request, "distributor/request.html", context)
            else:
                messages.info(request, "Invalid Password")
                return redirect('login')
        else:
            messages.info(request, "Invalid Username")
            return redirect('login')
    else:
        return render(request, 'distributor/login.html')

def add_request(request):
    if request.method == 'POST':
        request_name = request.POST['request_name']
        request_price = request.POST['request_price']
        request_details = request.POST['request_details']

        # Create a new Requests object and save it to the database
        Requests.objects.create(
            requestName=request_name,
            requestPrice=request_price,
            requestDetails=request_details
        )

        # Redirect to a success page or any other page you want
        return redirect('home')

    return render(request, 'distributor/add_request.html')

def req(request):
    return redirect('add_request')

def all_requests(request):
    all_requests = Requests.objects.all()
    context = {
        'requests': all_requests
    }
    return render(request, 'distributor/show.html', context)
