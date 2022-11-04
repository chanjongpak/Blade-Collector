from django.shortcuts import render
from django.http import HttpResponse

# Blade data

class Blade:
    def __init__(self,)


def home(request):
    return HttpResponse('<h1>Hello! Welcome to BladeCollector</h1>')

def about(request):
    return render(request, 'about.html')

def index(request):
    return render(request, 'blades/index.html', {'blades': blades})