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
# Formulaire pour mettre à jour le profil de l'utilisateur
class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="Nom", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label="Message", widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))

