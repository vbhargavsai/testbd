from django.shortcuts import render
from .models import tester
from .forms import testing
from django.http import HttpResponse

# Create your views here.

def insert(request):
    if request.method=="POST":
        form=testing(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("data saved")
    else:
        form=testing()
        return render(request,'input.html',{'f':form})
