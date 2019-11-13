from django.contrib import admin
from django.urls import path, include
from accounts.views import SignUpView


urlpatterns = [
    path('signup', SignUpView.as_view(), name='signup-form')
]
