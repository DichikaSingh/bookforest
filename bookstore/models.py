from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=255,null=True, blank=True)
    book_category = models.CharField(max_length=100)
    sub_category = models.CharField(max_length=100,null=True, blank=True)
    subject = models.CharField(max_length=100 ,null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    is_donated = models.BooleanField(default=False,null=True, blank=True)
    entry_date = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to='media/%Y/%m/', null=True, blank=True,max_length=255)
    book_type = models.CharField(max_length=50)
    on_sell = models.BooleanField(default=True,null=True, blank=True)

    def __str__(self):
        return self.book_name
