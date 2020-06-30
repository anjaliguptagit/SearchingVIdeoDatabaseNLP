from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def nlp(request):
    return render(request,'demoapp/nlp.html')