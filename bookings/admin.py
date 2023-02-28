from django.contrib import admin
from bookings.models import Event, Booking
# Register your models here.

admin.site.register(Event)
admin.site.register(Booking)