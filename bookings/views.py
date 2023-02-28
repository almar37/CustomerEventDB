from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Booking, Event
from .forms import EventForm, BookingForm

def index(request):
    return render(request, 'baseBooking.html')

def booking_mgnt(request):
    bookings = Booking.objects.all()
    return render(request, 'booking_mgnt/booking_mgnt.html',{'bookings': bookings})

def event_mgnt(request):
    events = Event.objects.all()
    return render(request, 'event_mgnt/event_mgnt.html', {'events': events})

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save()
            print('Successfully added Event')
            return event_mgnt(request)
            # render(request, 'event_mgnt/event_mgnt.html', {'event_mgnt': event_mgnt})
    else:
        form = EventForm()
        print('Failed to add event.')
    return render(request, 'event_mgnt/create_event.html', {'form': form})

def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        if 'confirm' in request.POST:
            event.delete()
        return redirect('event_mgnt')
    return render(request, 'delete_event.html', {'event': event})

def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            event = form.save()
            print('Successfully added Booking')
            return booking_mgnt(request)
            # render(request, 'event_mgnt/event_mgnt.html', {'event_mgnt': event_mgnt})
    else:
        form = BookingForm()
        print('Failed to add booking.')
    return render(request, 'booking_mgnt/create_booking.html', {'form': form})