from django.contrib import admin
from .models import Company, Customer
# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['name','company','age','place']

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display=['cmp_name','location']