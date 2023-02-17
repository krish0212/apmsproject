from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse
from .models import ParkingSlot,User
from .forms import BookingForm 
import pandas as pd
import sqlite3
from django.contrib import messages

con=sqlite3.connect('apms_db.sqlite3')
wb=pd.ExcelFile('C:/Users/krishna/Documents/anpr.xlsx')
for sheet in wb.sheet_names:
        df=pd.read_excel('C:/Users/krishna/Documents/anpr.xlsx',sheet_name=sheet)
        df.to_sql(sheet,con, index=False,if_exists="replace")
       #print(f'{df} inserted successfully')
con.commit()
con.close()


def available_slots(request):
    available_slots = ParkingSlot.objects.filter(is_available=True)
    booked_slots = ParkingSlot.objects.filter(is_available=False)
    context = {'slots': available_slots,'booked_slots': booked_slots}
    for slot in available_slots:
        print(f"Slot number: {slot.slot_number}")
    return render(request, 'available_slots.html',context)

def book_slot(request, slot_id):
    slot = get_object_or_404(ParkingSlot, id=slot_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # update the slot availability and show a confirmation page
            slot.is_available = False
            slot.booked_by = form.cleaned_data['name']
            slot.save()
            return redirect('booking_confirmation', slot_id=slot_id, name=form.cleaned_data['name'], email=form.cleaned_data['email'])
    else:
        form = BookingForm(initial={'slot_number': slot.slot_number})
    return render(request, 'book_slot.html', {'slot': slot, 'form': form})

def confirmation(request, slot_id, name, email):
    return render(request, 'confirmation.html', {'slot_id': slot_id, 'name': name, 'email': email})

def release_slot(request,slot_id):
    slot = get_object_or_404(ParkingSlot, id=slot_id)
    slot.is_available = True
    slot.booked_by = ''
    slot.save()
    return redirect('available_slots')
