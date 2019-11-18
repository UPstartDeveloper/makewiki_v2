from django.contrib import admin
from django.urls import path, include
from accounts.views import SignUpView
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


urlpatterns = [
    path('signup', SignUpView.as_view(), name='signup-form'),
    # Inspiration for these URL patterns goes to Corey Schafer's video tutorial: https://youtu.be/-tyBEsHSv7w
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"), name="password_reset"),
    path('reset-password/done/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_done.html"), name="password_reset_done"),
    path('reset-password-confirm/<uidb64/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="acccounts/password_reset_confirm.html"), name="password_reset_confirm"),

]
