from django.db import models

from Hotel.models import Hotel

# Menu Model
class Menu(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'menu'

    # Set Name of Menu
    def set_name(self, name):
        self.name = name
    
    # Set Price of Menu
    def set_price(self, price):
        self.price = price
    
    # Set Description of Menu
    def set_description(self, description):
        self.description = description