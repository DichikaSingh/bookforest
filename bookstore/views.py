from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Book
# Create your views here.



@login_required
def sell(request):

    try:
        if request.method=="POST":
            seller = request.user
            book_name =  request.POST.get('bookname')
            book_category =  request.POST.get('bookCategory')
            sub_category =  request.POST.get('subCategory')
            subject =  request.POST.get('subject')
            price =  request.POST.get('price')
            is_donated = request.POST.get('donate')
            picture =  request.FILES.get('book_image')
            book_type = request.POST.get('bookType')
            
            book = Book.objects.create( seller=seller,book_name=book_name,book_category=book_category,sub_category=sub_category,subject=subject,price=price,is_donated=is_donated,picture=picture,book_type=book_type
            )
            book.save()
    except:
            
            return render(request,"sell.html")




    return render(request,"sell.html")