#from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.http.response import StreamingHttpResponse
from django.core.files.storage import FileSystemStorage
from .models import ParkingLot 
from .forms import ParkingLotForm

def index(request):
    return render(request, 'E:/pyproject/apmsproject/apms/templates/accounts_main.html')

def create_parking_lot(request):
    if request.method == 'POST':
        form = ParkingLotForm(request.POST)
        if form.is_valid():
            parking_lot = ParkingLot.objects.create(
                rows=form.cleaned_data['rows'],
                columns=form.cleaned_data['columns'],
            )
            return redirect('view_parking_lot', id=parking_lot.id)
    else:
        form = ParkingLotForm()
    return render(request, 'create_parking_lot.html', {'form': form})

def get_slots(self):
    return [[ParkingLot.objects.get(parking_lot=self, row=i, column=j)
             for j in range(self.columns)] for i in range(self.rows)]
    
def view_parking_lot(request, id):
    parking_lot = ParkingLot.objects.get(id=id)
    slots = parking_lot.get_slots()
    context = {'parking_lot': parking_lot, 'slots': slots}
    return render(request, 'parking_lot.html', context)

def park_car(request, id):
    parking_lot = ParkingLot.objects.get(id=id)
    slots = parking_lot.get_slots()
    for i in range(parking_lot.rows):
        for j in range(parking_lot.columns):
            if not slots[i][j]:
                slots[i][j] = True
                parking_lot.slots = str(slots)
                parking_lot.save()
                return redirect('view_parking_lot', id=parking_lot.id)
    # all slots are occupied
    return render(request, 'full.html', {'parking_lot': parking_lot})

def checkout_car(request, id, row, column):
    parking_lot = ParkingLot.objects.get(id=id)
    slots = parking_lot.get_slots()
    slots[row][column] = False
    parking_lot.slots = str(slots)
    parking_lot.save()
    return redirect('view_parking_lot', id=parking_lot.id)

def admin_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request,user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'admin_login.html', d)


def Logout(request):
    logout(request)
    return redirect('index')







