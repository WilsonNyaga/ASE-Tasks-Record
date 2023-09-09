# views.py in your app directory
from django.shortcuts import render, redirect
from .models import Aircraft
from .forms import AircraftForm  # Import your form

def add_aircraft(request):
    if request.method == 'POST':
        form = AircraftForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('aircraft_list')  # Redirect to the list view after successful submission
    else:
        form = AircraftForm()

    return render(request, 'myapp/add_aircraft.html', {'form': form})

def edit_aircraft(request, aircraft_id):
    aircraft = Aircraft.objects.get(id=aircraft_id)

    if request.method == 'POST':
        form = AircraftForm(request.POST, instance=aircraft)
        if form.is_valid():
            form.save()
            return redirect('aircraft_list')  # Redirect to the list view after successful submission
    else:
        form = AircraftForm(instance=aircraft)

    return render(request, 'myapp/edit_aircraft.html', {'form': form, 'aircraft': aircraft})

# views.py in your app directory
from django.shortcuts import render
from .models import Aircraft

def display_all_data(request):
    aircraft = Aircraft.objects.all()
    return render(request, 'myapp/all_data.html', {'aircraft': aircraft})

# views.py in your app directory
from django.shortcuts import render
from django.core.mail import send_mail  # Import the send_mail function
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data, e.g., send an email
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['wilsonnyaga2@gmail.com']  # Replace with your Gmail address

            if cc_myself:
                recipients.append(sender)

            send_mail(subject, message, sender, recipients)

            # Redirect or display a success message
            # For example, you can redirect to a thank you page
            return redirect('thank_you')  # Change 'thank_you' to the appropriate URL pattern name
    else:
        form = ContactForm()

    return render(request, 'myapp/contact.html', {'form': form})
