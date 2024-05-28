from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.TextField()
    role = models.CharField(max_length=255)
    access_token = models.TextField()

    class Meta:
        db_table = 'users'
    
    # Set Name
    def set_name(self, name):
        self.name = name
    # Set Password
    def set_password(self, password):
        self.password = make_password(password)
