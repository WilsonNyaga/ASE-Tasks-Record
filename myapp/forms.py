# forms.py in your app directory
from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

# myapp/forms.py
from django import forms
from .models import Aircraft

class AircraftForm(forms.ModelForm):
    class Meta:
        model = Aircraft
        fields = ['job_number', 'registration', 'client', 'unit_description_name', 'unit_description_part_number', 'unit_description_serial_number', 'reported_snag', 'work_done']  # Define the fields you want in the form
