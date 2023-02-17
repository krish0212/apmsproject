from django import forms
from .models import  ParkingLot

class ParkingLotForm(forms.Form):
    rows = forms.IntegerField(min_value=1)
    columns = forms.IntegerField(min_value=1)
    #occupied= forms.BooleanField()
    class Meta:
        model = ParkingLot
        fields =['rows','columns','slots']