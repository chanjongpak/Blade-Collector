from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Blade
from .forms import MaintenanceForm

# Blade data

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def blades_index(request):
    blades = Blade.objects.all()
    return render(request, 'blades/index.html', {'blades': blades})

def blade_detail(request, blade_id):
    blade = Blade.objects.get(id=blade_id)
    maintenance_form = MaintenanceForm()
    return render(request, 'blades/detail.html', {'blade': blade, 'maintenance_form': maintenance_form})

def add_maintenance(request, blade_id):
    form = MaintenanceForm(request.POST)
    if form.is_valid():
        new_maintenance = form.save(commit=False)
        new_maintenance.blade_id = blade_id
        new_maintenance.save()
    return redirect('detail', blade_id=blade_id)

class BladeCreate(CreateView):
    model = Blade
    fields = '__all__'

class BladeUpdate(UpdateView):
    model = Blade
    fields = ['type', 'weight', 'flexibility', 'description']

class BladeDelete(DeleteView):
    model = Blade
    success_url = '/blades/'