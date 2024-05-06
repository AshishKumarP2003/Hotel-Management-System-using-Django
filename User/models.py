from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.TextField()
    role = models.CharField(max_length=255)
    access_token = models.TextField()

    class Meta:
        db_table = 'users'
    
    def set_name(self, name):
        self.name = name

    def set_password(self, password):
        self.password = password
