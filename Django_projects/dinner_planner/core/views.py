
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone

from datetime import datetime
from datetime import date
import calendar

# Create your views here.
from .models import Plate

days = {1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday',7:'Sunday'}
months = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
month_days={'January':31,'February':28,'March':31,'April':30,'May':31,'June':30,'July':31,'August':31,'September':30,'October':31,'November':30,'December':31}
def index(request):
    plates = Plate.objects.all()
    time = timezone.now()
    print(time)
    day_index = date.isoweekday(time)
    day = days[day_index]
    print(day)
    mon_index=datetime.now().month
    month = months[mon_index]
    days_in_month=month_days[month]
    day_num=datetime.now().day
    year = datetime.now().year
    first_day_index=date(year, mon_index, 1).isoweekday()    
    print(first_day_index)

    context = {'plates': plates, 'day': day, 'month':month, 'day_index':day_index, 'days_in_month':days_in_month, 'day_num':day_num, 'first_day_index':first_day_index+1, 'year':year}

    return render(request,'core/index.html', context)

def add(request):
    day = request.POST['date']
    print(day)
    prot = request.POST['protein']
    print(prot)
    star = request.POST['starch']
    print(star)
    vegg = request.POST['veggie']
    print(vegg)
    sauc = request.POST['sauce']
    print(sauc)
    extr = request.POST['extra']
    print(extr)
    p = Plate(date_created=timezone.now(),date=day,protein=prot,starch=star,veggie=vegg,sauce=sauc,extra=extr)
    p.save()
    context = {'plates':Plate.objects.all()}
    return HttpResponseRedirect (reverse('core:index'), context)

def edit(request):
    id = request.POST['edit']
    p = Plate.objects.get(pk=id)
    p.date = request.POST['date']
    p.protein = request.POST['protein']
    p.starch = request.POST['startch']
    p.veggie = request.POST['veggie']
    p.sauce = request.POST['sauce']
    p.extra = request.POST['extra']
    p.date_modified = timezone.now()
    p.save()
    context = {'plates':Plate.objects.all()}
    return HttpResponseRedirect (reverse('core:index'), context)


def delete(request):
    id = request.POST['delete']
    p = Plate.objects.get(pk=id)
    p.delete()
    context = {'platess':Plate.objects.all()}
    return HttpResponseRedirect (reverse('core:index'), context)
