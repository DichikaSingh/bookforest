from django.contrib import admin
from .models import Info

@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'address','city','zipcode','state','Latitude','Longitude')  # Customize the displayed fields in the admin list view
    # Add any other configurations you may need
