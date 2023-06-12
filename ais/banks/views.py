from django.shortcuts import render


def banks(request):
    return render(request, 'banks/banks.html')