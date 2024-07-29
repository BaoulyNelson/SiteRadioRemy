# forms.py
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'content']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Votre nom (optionnel)'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Votre email (optionnel)'}),
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Écrivez votre commentaire ici...'}),
        }
