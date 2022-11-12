from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Blade, Accessory
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
    accessories_blade_doesnt_have = Accessory.objects.exclude(id__in = blade.accessories.all().values_list('id'))
    maintenance_form = MaintenanceForm()
    return render(request, 'blades/detail.html', {'blade': blade, 'maintenance_form': maintenance_form, 'accessories': accessories_blade_doesnt_have})

def add_maintenance(request, blade_id):
    form = MaintenanceForm(request.POST)
    if form.is_valid():
        new_maintenance = form.save(commit=False)
        new_maintenance.blade_id = blade_id
        new_maintenance.save()
    return redirect('detail', blade_id=blade_id)

def assoc_accessory(request, blade_id, accessory_id):
    Blade.objects.get(id=blade_id).accessories.add(accessory_id)
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

class AccessoryList(ListView):
    model = Accessory

class AccessoryCreate(CreateView):
    model = Accessory
    fields = '__all__'

class AccessoryDetail(DetailView):
    model = Accessory

class AccessoryUpdate(UpdateView):
    model = Accessory
    fields = ['name', 'color']

class AccessoryDelete(DeleteView):
    model = Accessory
    success_url = '/accessories/'