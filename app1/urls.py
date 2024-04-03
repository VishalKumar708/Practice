from django.contrib import admin
from django.urls import path
from .views import register_user_form

urlpatterns = [
    path('user_register/', register_user_form)
]
