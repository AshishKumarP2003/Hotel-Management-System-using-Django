from django.db import models

from Room.models import Room
from Hotel.models import Hotel
from Guest.models import Guest

# Create your models here.
class Booking(models.Model):
    guest_id = models.ForeignKey(Guest, on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    check_in_time = models.DateTimeField(max_length=255, null=True)
    check_out_time = models.DateTimeField(max_length=255, null=True)
    amount = models.IntegerField(default=0)

    class Meta:
        db_table = 'booking'

    def set_check_out_time(self, check_out_time):
        self.check_out_time = check_out_time
    
    def set_amount(self, amount):
        self.amount = amount