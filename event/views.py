from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EventForm
from .models import Event
from django.contrib.auth.decorators import login_required
from .credentials import *


# Create your views here.

@login_required(login_url='login-url')
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'event added  successfully')
            return redirect('donate-url')
        else:
            messages.error(request, 'event saving failed')
    else:
        form = EventForm()
    return render(request, 'events/add_events.html', {'form': form})


def donate(request):
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'events/donate.html', context)


def update_event(request, id):
    event = Event.objects.get(id=id)
    context = {
        'event': event
    }
    if request.method == 'POST':
        event_name = request.POST.get('event_name')
        event_description = request.POST.get('event_description')
        event_date = request.POST.get('event_date')
        venue = request.POST.get('venue')
        minimum_amount = request.POST.get('minimum_amount')
        image = request.FILES.get('image')
        event.event_name = event_name
        event.event_description = event_description
        event.event_date = event_date
        event.venue = venue
        event.minimum_amount = minimum_amount
        event.image = image
        event.save()
        messages.success(request, 'event updated successfully')
        return redirect('donate-url')

    return render(request, 'events/update_events.html', context)


def delete_event(request, id):
    event = Event.objects.get(id=id)
    event.delete()
    messages.info(request, 'Event deleted successfully')
    return redirect('donate-url')


def pay(request, id):
    event = Event.objects.get(id=id)

    if request.method == "POST":
        phone_number = request.POST['phone_number']
        minimum_amount = event.minimum_amount
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPassword.Business_short_code,
            "Password": LipanaMpesaPassword.decode_password,
            "Timestamp": LipanaMpesaPassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": minimum_amount,
            "PartyA": phone_number,
            "PartyB": LipanaMpesaPassword.Business_short_code,
            "PhoneNumber": phone_number,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "UnashamedHeart Foundation",
            "TransactionDesc": "Donation"
        }

        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("transaction made successfully")

    return render(request, 'payment/pay.html', {'event': event})


def pay_option2(request):
    if request.method == "POST":
        phone_number = request.POST['phone_number']
        minimum_amount = request.POST['minimum_amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPassword.Business_short_code,
            "Password": LipanaMpesaPassword.decode_password,
            "Timestamp": LipanaMpesaPassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": minimum_amount,
            "PartyA": phone_number,
            "PartyB": LipanaMpesaPassword.Business_short_code,
            "PhoneNumber": phone_number,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "UnashamedHeart Foundation",
            "TransactionDesc": "Donation"
        }

        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("transaction made successfully")

    return render(request, 'payment/pay2.html')
