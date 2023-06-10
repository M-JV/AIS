from django.urls import path
from . import views


urlpatterns = [
    path('policy/policy.html', views.policy, name='policy'),
]