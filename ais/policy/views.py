from django.shortcuts import render

# Create your views here.
def policy(request):
    # Your contact view code here
    return render(request, 'policy/policy.html')
