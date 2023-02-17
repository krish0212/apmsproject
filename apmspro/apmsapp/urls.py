from django.urls import path
from .views import book_slot,release_slot,confirmation,available_slots ,update_parking_lot

#app_name = 'parking'

urlpatterns = [
    path('update-parking-lot/', update_parking_lot, name='update_parking_lot'),   
    path('', available_slots, name='available_slots'),
    #path('occupied_slots/', occupied_slots, name='occupied_slots'),
    path('book/<int:slot_id>/', book_slot, name='book_slot'),
    path('confirmation/<int:slot_id>/<str:name>/<str:email>/', confirmation, name='booking_confirmation'),
    #path('booked/', booked_slots_view, name='booked_slots'),
    path('release/<int:slot_id>/', release_slot, name='release_slot'),
    ]

