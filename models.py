from django.db import models
#from django.contrib.auth.models import User

# Create your models here.

class ParkingLot(models.Model):
    rows = models.PositiveSmallIntegerField()
    columns = models.PositiveSmallIntegerField()
   # occupied = models.BooleanField(default=False)
    slots = models.TextField()
    
    def save(self, *args, **kwargs):
        slots = []
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                row.append(True)
            slots.append(row)
        self.slots = str(slots)
        super().save(*args, **kwargs)
    
    def get_slots(self):
        return eval(self.slots)
    
    def _str_(self):
        return f'Parking Lot ({self.rows}x{self.columns})'
