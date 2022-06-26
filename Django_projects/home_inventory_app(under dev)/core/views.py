
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render, get_object_or_404
from core.models import SuperCategory, Category, SubCategory, Item


# Create your views here.
def index(request):
    items = Item.objects.all()
    context = {'items': items }
    return render(request,'core/index.html',context)

