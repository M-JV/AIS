from django.urls import path
from . import views


urlpatterns = [
    path('banks/banks.html', views.banks, name='banks'),
]