from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.log_in, name='login'),
    path('signup/', views.sign_up, name='signup'),
    path('', views.home, name='home'),
    path('request/', views.add_request, name='add_request'),
    path('req/', views.req, name='req'),
     path('all-requests/', views.all_requests, name='all_requests'),
]
