from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'image','username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'is_admin']


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form_control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form_control'}))

