from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("<h1>1st index page project date 06-04-2021</h1>")
def samp1(request):
    return render(request,"sample1.html")
def facto(request,num):
    fact=1
    for i in range(1,int(num)+1):
        fact*=i
    return HttpResponse(f"<h1>fact the {num} is {fact}")
def add(request,num1,num2):
    try:
        num1=int(num1)
    except:
        num1=float(num1)
    try:
        num2=int(num2)
    except:
        num2=float(num2)
    return HttpResponse(num1+num2)
def carry_data(request,data):
    return HttpResponse(f"<h1>the acrried data is {data}")

# Create your views here.
