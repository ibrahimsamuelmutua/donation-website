"""
URL configuration for unashameddCharityOrganization project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from . import views as sam

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sam.home, name='home-url'),
    path('about/', sam.about, name='about-url'),
    path('services/', sam.services, name='services-url'),
    path('gallery/', sam.gallery, name='gallery-url'),
    path('team/', sam.team, name='team-url'),
    path('donate/', sam.donate,name='donate-url'),
    path('contact/',sam.contact,name='contact-url'),
    path('register/',sam.register, name='register-url'),
    path('login/', sam.loginuser, name='login-url'),
]