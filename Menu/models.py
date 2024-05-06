from django.db import models

from Hotel.models import Hotel

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'menu'

    def set_name(self, name):
        self.name = name
    
    def set_price(self, price):
        self.price = price
    
    def set_description(self, description):
        self.description = description