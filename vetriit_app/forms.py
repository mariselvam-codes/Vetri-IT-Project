from django import forms
from .models import Enquiry

SERVICE_CHOICES = [
    ("Web Development", "Web Development"),
    ("Software Development", "Software Development"),
    ("Digital Marketing", "Digital Marketing"),
]

class EnquiryForm(forms.ModelForm):
    service = forms.ChoiceField(choices=SERVICE_CHOICES)

    class Meta:
        model = Enquiry
        fields = ['name', 'email', 'phone', 'message', 'service']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter Email Address'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter Mobile Number'}),
            'message': forms.Textarea(attrs={'placeholder': 'Enter the Message', 'rows':4}),
        }
