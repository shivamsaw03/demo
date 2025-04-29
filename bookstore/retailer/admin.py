from django.contrib import admin

# Register your models here.
from .models import Retailer

@admin.register(Retailer)
class RetailerAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile_no', 'date_of_joining', 'total_sales','address' ,'is_active')
    list_filter = ('is_active', 'date_of_joining')
    search_fields = ('name', 'mobile_no', 'address')
    list_editable = ('total_sales', 'is_active')
    date_hierarchy = 'date_of_joining'
    ordering = ('-date_of_joining',)
