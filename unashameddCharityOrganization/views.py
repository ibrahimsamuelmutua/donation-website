from django.shortcuts import render
from django.core.mail import send_mail


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
    if request.method == 'POST':
        sender_name = request.POST['name']
        sender_email = request.POST['email']
        sender_message = request.POST['message']

        send_mail(
            sender_name,
            sender_email,
            sender_message,
            ["samuelmutuaibrahim@gmail.com", "ondeyostephen0@gmail.com"]
        )
        return render(request,'contact.html',{'sender_name':sender_name})
    return render(request, 'contact.html')
