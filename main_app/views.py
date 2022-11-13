from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Blade, Accessory
from .forms import MaintenanceForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def signup(request):
    error_messsage = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_messsage = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message':error_messsage}
    return render(request, 'registration/signup.html', context)

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def blades_index(request):
    blades = Blade.objects.filter(user=request.user)
    return render(request, 'blades/index.html', {'blades': blades})

@login_required
def blade_detail(request, blade_id):
    blade = Blade.objects.get(id=blade_id)
    accessories_blade_doesnt_have = Accessory.objects.exclude(id__in = blade.accessories.all().values_list('id'))
    maintenance_form = MaintenanceForm()
    return render(request, 'blades/detail.html', {'blade': blade, 'maintenance_form': maintenance_form, 'accessories': accessories_blade_doesnt_have})

@login_required
def add_maintenance(request, blade_id):
    form = MaintenanceForm(request.POST)
    if form.is_valid():
        new_maintenance = form.save(commit=False)
        new_maintenance.blade_id = blade_id
        new_maintenance.save()
    return redirect('detail', blade_id=blade_id)

@login_required
def assoc_accessory(request, blade_id, accessory_id):
    Blade.objects.get(id=blade_id).accessories.add(accessory_id)
    return redirect('detail', blade_id=blade_id)

class BladeCreate(LoginRequiredMixin, CreateView):
    model = Blade
    fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BladeUpdate(LoginRequiredMixin, UpdateView):
    model = Blade
    fields = ['type', 'weight', 'flexibility', 'description']

class BladeDelete(LoginRequiredMixin, DeleteView):
    model = Blade
    success_url = '/blades/'

class AccessoryList(LoginRequiredMixin, ListView):
    model = Accessory

class AccessoryCreate(LoginRequiredMixin, CreateView):
    model = Accessory
    fields = '__all__'

class AccessoryDetail(LoginRequiredMixin, DetailView):
    model = Accessory

class AccessoryUpdate(LoginRequiredMixin, UpdateView):
    model = Accessory
    fields = ['name', 'color']

class AccessoryDelete(LoginRequiredMixin, DeleteView):
    model = Accessory
    success_url = '/accessories/'

