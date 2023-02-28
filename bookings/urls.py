from django.urls import path, include
from . import views
from .views import create_event, delete_event, create_booking
app_name = 'bookings'

urlpatterns = [
    path('', views.index, name='index'),
    path('booking_mgnt/', views.booking_mgnt, name='booking_mgnt'),
    path('event_mgnt/', views.event_mgnt, name='event_mgnt'),
    path('event_mgnt/create_event/', create_event, name='create_event'),
    path('event_mgnt/create_booking/', create_booking, name='create_booking'),
    path('event/<int:event_id>/delete/', delete_event, name='delete_event'),
    ]

