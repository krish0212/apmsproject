from django import forms
#from .models import ParkingLot
from .models import ParkingSlot

  
class BookingForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    #slot_number = forms.IntegerField()
