from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def gallery(request):
    return render(request, 'gallery.html')


def team(request):
    return render(request, 'team.html')


def donate(request):
    return render(request, 'donate.html')


def contact(request):
    return render(request, 'contact.html')


def register(request):
    return render(request, 'register.html')


def loginuser(request):
    return render(request, 'login.html')
