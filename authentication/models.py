from django.contrib.auth.models import User
from django.db import models

class Info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(max_length=200,null=True, blank=True)
    
    city = models.CharField(max_length=200,blank=True, null=True)
    zipcode = models.CharField(max_length=200,blank=True, null=True)
    state = models.CharField(max_length=200,blank=True, null=True)
    edited_at = models.DateTimeField(auto_now=True)
    Latitude = models.CharField(max_length=200,blank=True, null=True)
    Longitude = models.CharField(max_length=200,blank=True, null=True)
    def __str__(self):
        return f'Info for {self.user.username}'








   

    