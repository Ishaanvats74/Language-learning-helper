from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 

def Home(request):
    return HttpResponse('Home page')

def About_us(request):
    return HttpResponse('About Us Page')