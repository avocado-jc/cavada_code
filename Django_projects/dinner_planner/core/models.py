from django.db import models

# Create your models here.
from django.utils import timezone
from datetime import date
import datetime

days = {1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday',7:'Sunday'}
months = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
class Plate(models.Model):
    date_created = models.DateTimeField(verbose_name="date created")
    date_modified = models.DateTimeField(verbose_name="date modified", blank=True,null=True)
    date = models.DateField(verbose_name="date")
    protein = models.CharField(max_length=50,verbose_name='protein')
    starch = models.CharField(max_length=50,verbose_name='starch')
    veggie = models.CharField(max_length=50,verbose_name='vegetable')
    sauce = models.CharField(max_length=50,verbose_name='sauce')
    extra = models.CharField(max_length=50,verbose_name='extra', blank=True,null=True)
    
    def __str__(self):
        the_date = self.date
        day_index = date.isoweekday(the_date)
        day = days[day_index]
        print(day)
        mon_index = the_date.month
        print(mon_index)
        month = months[mon_index]
        day_num = the_date.day
        return str(day) + ' dinner (' + month + ' ' + str(day_num) + ')'
    class Meta:
        ordering = ('date',)