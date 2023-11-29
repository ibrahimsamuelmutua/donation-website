from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'projects.html')


def gallery(request):
    return render(request, 'gallery.html')


def team(request):
    return render(request, 'team.html')


def donate(request):
    return render(request, 'events/donate.html')


def contact(request):
    return render(request, 'contact.html')






