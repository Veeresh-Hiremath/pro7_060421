from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("<h1>2nd index page project date 06-04-2021</h1>")
def samp2(request):
    return render(request,"sample2.html")

# Create your views here.
