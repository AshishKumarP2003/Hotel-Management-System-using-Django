from django.db import models

from Hotel.models import Hotel

# Guest Model
class Guest(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=255)
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    # Guest Table Name
    class Meta:
        db_table = 'guest'

    # Set Guest Name
    def set_name(self, name):
        self.name = name
    
    # Set Guest Email
    def set_email(self, email):
        self.email = email
    
    # Set Guest Phone Number
    def set_phone_number(self, phone_number):
        self.phone_number = phone_number