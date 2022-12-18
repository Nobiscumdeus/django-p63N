from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request,'basic/home.html')
def html(request):
    return render(request,'basic/basic.html')