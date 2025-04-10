from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render (request,'website/index.html')
# i need to create a these pages as an assignments

def about(request):
    return render(request,'website/about.html')

def contact(request):
    return HttpResponse("hello Contact Page")