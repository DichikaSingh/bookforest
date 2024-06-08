"""
URL configuration for bookforests project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from authentication.views import *
from bookforests.views import *
from django.conf import settings
from django.conf.urls.static import static
from bookstore.views import *
from payment.views import*
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('logout/', logout_page),


    path('',home,name='home'),
    path('shop/',shop,name='shop'),
    path('sell/',sell,name='sell'),

     path('paymenthandler/', paymenthandler, name='paymenthandler'),
    path('detail/<var>',detail,name='detail'),
    path('profile/',profile),
    path('profile_on_sell/',profile_on_sell),
    path('delete_book/<id>/',delete_book),
    path('update_on_sell/<bookId>/',update_on_sell),
    




] + static( settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
