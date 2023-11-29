from django.shortcuts import render, redirect
from .forms import LoginForm, SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User


# Create your views here.
def loginuser(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'welcome, {username}')
                return redirect('home-url')


            else:
                messages.success(request, 'error')
                return redirect('login-url')
        else:
            messages.success(request, 'error')
            return redirect('login-url')
    else:
        form = LoginForm()
        return render(request, 'authentication/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('login-url')
        else:
            messages.success(request, 'error')

    else:
        form = SignUpForm()
    return render(request, 'authentication/register.html', {'form': form})


def log_out(request):
    logout(request)
    messages.success(request, 'you have logged out')
    return redirect('home-url')


def member_profile(request, id):
    user = User.objects.get(id=id)
    context = {
        'user': user,
    }
    if request.method == 'POST':
        image = request.FILES.get('image')
        user.image = image
        user.save()
        messages.success(request, 'image updated successfully')
    else:
        pass
    return render(request, 'member_profile/member_profile.html', context)
