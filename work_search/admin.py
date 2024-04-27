from django.contrib import admin
from .models import Job
from django.contrib.admin import ModelAdmin
# Register your models here.
# admin.site.register(Job)

@admin.register(Job)
class JobAdmin(ModelAdmin):
    list_display = ('id', 'title', 'url', 'platform')
    list_filter = ('id', )
    list_editable = ('platform', )
    search_fields = ('title', )

