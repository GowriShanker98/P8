from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Welcome to the Index Page")

def home(request):
    return render(request,"myapp/base.html",{"name":"CHITI"})

def child(request):
    return render(request,"child.html")

def sample(request):
    return render(request,"myapp/sample.html")