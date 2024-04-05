from django.contrib import admin
from django.urls import path
from .views import register_user_form, get_contact_form, get_details

urlpatterns = [
    path('user_register/', register_user_form),
    path('get_contact_form/', get_contact_form),
    path('get_details/', get_details)
]
