from django.shortcuts import render
import json

# Create your views here.
def home(request):
    
    return render(request,'home.html')