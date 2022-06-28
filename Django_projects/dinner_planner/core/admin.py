from django.contrib import admin

# Register your models here.

from .models import Plate
# Register your models here.
admin.site.register([Plate])