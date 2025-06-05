from django import forms
from .models import EmailSubscriber

class EmailSignupForm(forms.ModelForm):
    class Meta:
        model = EmailSubscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter your email',
                'class': 'form-control'
            })
        }