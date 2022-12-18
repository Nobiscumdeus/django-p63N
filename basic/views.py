from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1> Finally, Chasfat Project$ Django applications are finding a space online after a long while </h1>')
