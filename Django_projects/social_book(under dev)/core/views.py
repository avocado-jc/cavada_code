from audioop import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from .models import Profile

def index(response):
    profiles = Profile.objects.all()
    context = {"profiles": profiles}
    return render (response,"index.html", context)

def sign_up(request):
    profiles = Profile.objects.all()
    context = {"profiles": profiles}
    # if request.method=="POST":
    #     username=request.POST["username"]
    #     email=request.POST["email"]
    #     p1=request.POST["password 1"]
    #     p2=request.POST["password 2"]
    #     if p1==p2:
    #         u = Profile(used=username,id_user=email,password=p1)
    #         u.save()
    #     else:
    #         return HttpResponseRedirect(reverse('core:index'))
    # else:
    #     return HttpResponseRedirect(reverse('core:index'))
    return render(request,"sign_up.html",context)

def profile(request):
    profiles = Profile.objects.all()
    context = {"profiles": profiles}
    return render(request,"profile.html",context)