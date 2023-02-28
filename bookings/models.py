from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BusinessProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=255)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=255)
    capacity = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    operator = models.ForeignKey(BusinessProfile, on_delete=models.CASCADE)


class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    number_of_tickets = models.IntegerField()
    payment_status = models.BooleanField(default=False)