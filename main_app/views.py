from django.shortcuts import render
from django.http import HttpResponse

# Blade data

class Blade:
    def __init__(self, name, type, weight, flexibility, description):
        self.name = name
        self.type = type
        self.weight = weight
        self.flexibility = flexibility
        self.description = description

blades = [
    Blade('Excalibur', 'Longsword', 4, 'Not Flexible', 'Legendary sword of King Arthur'),
    Blade('Durendal', 'Longsword', 3, 'Not Flexible', 'A historic sword wielded by Roland'),
    Blade('Ame-no-Habakiri', 'Katana', 2.6, 'Somewhat Flexible', "Legendary sword known to have beheaded 'Yamata-no-Orochi' more commonly known as eight-headed serpent")
]

def home(request):
    return HttpResponse('<h1>Hello! Welcome to BladeCollector</h1>')

def about(request):
    return render(request, 'about.html')

def blades_index(request):
    return render(request, 'blades/index.html', {'blades': blades})