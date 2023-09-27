from django.urls import path

from .views import *

urlpatterns = [
    path('', HomePage, name='homePage'),
    path('home/', HomePage, name='homePage'),
    path('register/', register, name='register'),
    
]
