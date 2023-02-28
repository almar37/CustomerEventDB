# bookings/forms.py

from django import forms
from .models import Event, Booking

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name','date', 'start_time', 'end_time', 'location', 'capacity', 'price', 'operator']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer_name','event', 'number_of_tickets', 'payment_status']
