from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import RateUs, Contact
# Register your models here.
@admin.register(Contact)
class ContactAdmin(ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'text')
    list_filter = ('id', )
    search_fields = ('id', 'full_name')

@admin.register(RateUs)
class RateAdmin(ModelAdmin):
    list_display = ('id', 'full_name', 'rate', 'description')
    list_filter = ('rate', )
    search_fields = ('id', 'full_name')

