from django.contrib import admin
from .models import Country
# Register your models here.
class CountryAdmin(admin.ModelAdmin):
    list_display=('name','code','color','flag')

admin.site.register(Country, CountryAdmin)
