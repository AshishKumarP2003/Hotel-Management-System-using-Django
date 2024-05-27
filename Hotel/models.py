from django.db import models

from User.models import User

# Hotel Model
class Hotel(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10)

    # Hotel Table Name
    class Meta:
        db_table = 'hotels' 
    
    # Get Name of Hotel.
    def get_name(self):
        return self.name
    
    # Set Name of Hotel.
    def set_name(self, name):
        self.name = name
    
    # Get Address of Hotel
    def get_address(self):
        return self.address

    # Set Address of Hotel.
    def set_address(self, address):
        self.address = address

    # Get Phone Number of Hotel
    def get_phone_number(self):
        return self.phone_number
    
    # Set Phone Number of Hotel
    def set_phone_number(self, phone_number):
        self.phone_number = phone_number


# Create your models here.
class HotelAdmin(models.Model):
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'hotel_admins' 
