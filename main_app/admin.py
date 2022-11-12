from django.contrib import admin
from .models import Blade, Maintenance, Accessory

# Register your models here.
admin.site.register(Blade)
admin.site.register(Maintenance)
admin.site.register(Accessory)