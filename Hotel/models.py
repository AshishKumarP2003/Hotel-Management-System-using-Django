from django.db import models

from User.models import User

# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10)

    class Meta:
        db_table = 'hotels' 
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    
    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number


# Create your models here.
class HotelAdmin(models.Model):
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'hotel_admins' 
