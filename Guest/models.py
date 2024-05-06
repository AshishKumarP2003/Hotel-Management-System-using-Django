from django.db import models

from Hotel.models import Hotel

# Create your models here.
class Guest(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=255)
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'guest'

    def set_name(self, name):
        self.name = name
    
    def set_email(self, email):
        self.email = email
    
    def set_phone_number(self, phone_number):
        self.phone_number = phone_number