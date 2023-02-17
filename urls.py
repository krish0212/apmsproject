from django.contrib import admin
from django.urls import path
from apms.views import *
from django.conf import settings
from django.conf.urls.static import static
#from django.urls import path
#from .views import index, reserve, release
#from apms import *
          
#app_name = 'conference_rooms'
#app_name = 'parking'
#app_name='admin_login'

urlpatterns = [
   #path('', index, name='index'),
   path('', index, name='index'),
   path('admin_login',admin_login,name='admin_login'),
   path('create/', create_parking_lot, name='create_parking_lot'),
    #path('parking_lot/<int:parking_lot_id>/occupy_slot/<int:row>/<int:column>/',occupy_slot, name='occupy_slot'),
   path('<int:id>/', view_parking_lot, name='view_parking_lot'),
   path('<int:id>/park/', park_car, name='park_car'),
   path('<int:id>/checkout/<int:row>/<int:column>/', checkout_car, name='checkout_car'),
   #reverse('parking:occupy_slot', args=[parking_lot_id, row, column]),
   #path('about',about,name='about'),
   #path('contact',contact,name='contact'),
   #path('admin_home',admin_home,name='admin_home'),
   path('logout',Logout,name='logout'),
   #path('change_password',change_password,name='change_password'), 
]