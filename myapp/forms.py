# forms.py in your app directory
from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

# myapp/forms.py
from django import forms
from .models import Aircraft  # Import the Aircraft model from models.py

class AircraftForm(forms.ModelForm):
    class Meta:
        model = Aircraft  # Specify the model for the form
        fields = ['registration', 'client', 'job_number', 'date']  # Define the fields you want in the form
