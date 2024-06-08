
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from bookstore.models import Book
import razorpay
from django.conf import settings

from django.views.decorators.csrf import csrf_exempt

# Create your views here.






client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))



def detail(request,var):
    book=Book.objects.get(id=var)
    if request.method =='POST':
        amount =   90000 # Amount in paise  
        currency = "INR"
        callback_url = '/paymenthandler/'    
        order = client.order.create(dict(amount=amount, currency=currency,payment_capture='1'))
        response_data = {
        "id": order["id"],
        "amount": order["amount"],
        "currency": order["currency"],
        "key": settings.RAZORPAY_API_KEY,
        "name": "Your Company Name",
        "callback_url": callback_url,}
        print("gfffj,gjhgjhgjhgjhgjhgjhgjhg")
        return render(request, "detail.html",{'data':response_data,'book':book})
    return render(request, "detail.html",{'book':book})






@csrf_exempt
def paymenthandler(request):
 
    # only accept POST request.
    if request.method == "POST":
        # get the required parameters from post request.
        payment_id = request.POST.get('razorpay_payment_id', '')
        razorpay_order_id = request.POST.get('razorpay_order_id', '')
        signature = request.POST.get('razorpay_signature', '')
        params_dict = {
            'razorpay_order_id': razorpay_order_id,
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
        }
            # verify the payment signature.
        result = client.utility.verify_payment_signature(params_dict)
        if result :  
            
            return render(request, 'payment_success.html')
        else:
            return render(request, 'payment_failed.html')
