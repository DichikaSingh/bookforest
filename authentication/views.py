from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.models import User
from .models import Info
from bookstore.models import Book

def logout_page(request):
    logout(request)
    return redirect("/")




def home(request):
    
    user=request.user
    try:
        book=Book.objects.filter(on_sell=True)
        data=SocialAccount.objects.get(user=user).extra_data
        return render(request, 'index.html',{'data':data,'books':book})
    except:
        book=Book.objects.filter(on_sell=True)
        return render(request, 'index.html',{'books':book})



def profile(request):
    user=request.user
    try:
        if request.method =='POST':
            phone_number=request.POST.get('phone_number')
            address=request.POST.get('address')
            if Info.objects.filter(user=user):
                update_info=Info.objects.get(user=user)
                update_info.phone_number=phone_number
                update_info.address=address
                update_info.save()
                return redirect('/profile/')
            else:
                Info.objects.create(user=user, phone_number=phone_number, address=address)
            return redirect('/profile/')
        else:
            data=SocialAccount.objects.get(user=user).extra_data
            return render(request,"profile.html",{"data":data})    
    except:
        return render(request,"profile.html")
    
    
def profile_on_sell(request):
    user=request.user
    books=Book.objects.filter(seller=user)
    
    return render(request,"profile_on_sell.html",{'books':books})
    

def delete_book(request,id):
    book=Book.objects.get(id=id)
    book.delete()
    return redirect('/profile_on_sell/')



def update_on_sell(request,bookId):
    book=Book.objects.get(id=bookId)
    if request.method =='GET':
        on_sell =request.GET.get('on_sell')
        if on_sell =='true':
            book.on_sell=True
        else: 
            book.on_sell=False
        book.save()
    return redirect('/profile_on_sell/')