from django.contrib import admin
from .models import Realtor
# Register your models here.

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'email', 'phone', 'hire_date')
    list_display_links = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('name', 'email')
    list_per_page = 25


admin.site.register(Realtor, RealtorAdmin)