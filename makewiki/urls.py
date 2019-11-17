"""makewiki URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
import django.contrib.auth.views as auth_views
from django.urls import path, include

"""
CHALLENGES:
    1. Uncomment the path() for the wiki app below. Use it to direct any request (except `/admin` URLs)
        to the the `wiki` app's URL configuration. Use the above docstring to guide you if you feel stuck.
    2. Make sure Django doesn't give you any warnings or errors when you execute `python manage.py runserver`.
"""
urlpatterns = [
    # Admin Site
    path('admin/', admin.site.urls),

    # Wiki App
    path('', include('wiki.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    # Accounts App
    path('registration/', include('accounts.urls')),
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"), name="password_reset")
]
