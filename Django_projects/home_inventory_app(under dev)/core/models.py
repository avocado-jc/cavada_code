from django.db import models

# Create your models here.

class SuperCategory(models.Model): # supplies, food, 
    name = models.CharField(max_length=50,verbose_name='supercatogory name')
    def __str__(self):
        return self.name

class Category(models.Model): # meat, dairy, snacks, dessert, frozen food, 
    supercategory = models.ForeignKey(SuperCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=50,verbose_name="category name")
    def __str__(self):
        return self.name
    

class SubCategory(models.Model): # beef, chicken, rice, flour, 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50,verbose_name='subcategory name')
    type = models.CharField(max_length=50,verbose_name='type')
    qty = models.PositiveIntegerField(verbose_name='quantity')
    def __str__(self):
        return self.name

class Item(models.Model): # 2lb Costco ground beef, bag of doritos, box of donuts, arm&hammer toothpaste 
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name='item name')
    desc = models.CharField(max_length=255, verbose_name='item description')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='item price')
    upc = models.CharField(max_length=12, verbose_name='item upc')
    record_date = models.DateTimeField(verbose_name="date item recorded")
    sell_by_date = models.DateField(verbose_name='item sell by date')
    expire_date = models.DateField(verbose_name='item expiration date')
    ct = models.PositiveIntegerField(verbose_name='item count',null=True,blank=True)
    discarded = models.BooleanField(verbose_name="discarded")
    def __str__(self):
        return self.name


