from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class ParkingSlot(models.Model):
    
    slot_number = models.CharField(max_length=50, unique=True)
   #slot_type = models.CharField(max_length=1, choices=SLOT_TYPE_CHOICES)
    is_available = models.BooleanField(default=True)
    #slots=models.IntegerField(null=True)      
    booked_by = models.CharField(max_length=50, blank=True)
    license_plate =models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.slot_number   
    
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateField()
    time =models.TimeField()
    direction = models.CharField (max_length=50, null=True)
    images= models.CharField(max_length=100, null=True)
    plateimages= models.CharField(max_length=100, null=True)
    plateresult= models.CharField(max_length=100, null=True)
   
    def __str__(self):
            return self.id

    