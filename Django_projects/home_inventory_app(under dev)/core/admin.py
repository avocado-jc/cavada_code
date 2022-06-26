from django.contrib import admin
from .models import SuperCategory,Category, SubCategory, Item
# Register your models here.
admin.site.register([SuperCategory,Category,SubCategory,Item])