from django.db import models

from Hotel.models import Hotel

# Create your models here.
class Room(models.Model):
    room_number = models.CharField(max_length=255)
    room_type = models.CharField(max_length=255)
    price_per_night = models.IntegerField()
    reserved = models.BooleanField(default=False)
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'room'

    def set_room_number(self, room_number):
        self.room_number = room_number
    
    def set_room_type(self, room_type):
        self.room_type = room_type
    
    def set_price_per_night(self, price_per_night):
        self.price_per_night = price_per_night