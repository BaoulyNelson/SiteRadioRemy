# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Obligatoire.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Obligatoire.')
    email = forms.EmailField(required=True, help_text='Obligatoire. Un email valide sera envoyé.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
