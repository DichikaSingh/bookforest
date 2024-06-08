
from django.conf import settings
from django.shortcuts import render

from bookstore.models import Book

def shop(request):
    book=Book.objects.filter(on_sell=True)
    return render(request,"shop.html",{'books':book})

