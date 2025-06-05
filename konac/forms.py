from django import forms
from .models import EmailSubscriber

class EmailSignupForm(forms.ModelForm):
    class Meta:
        model = EmailSubscriber
        fields = ['name', 'email']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Name',
                'class': 'form-input nameInput'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email Address*',
                'class': 'form-input emailInput'
            })
        }