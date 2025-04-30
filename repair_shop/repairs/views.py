from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Equipment
from .forms import EquipmentForm

def home(request):
    return render(request, 'repairs/home.html')

def register_equipment(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            equipment = form.save()
            return render(request, 'repairs/register.html', {
                'form': EquipmentForm(),
                'success': True,
                'equipment_id': equipment.id
            })
    else:
        form = EquipmentForm()
    return render(request, 'repairs/register.html', {'form': form})

def search_equipment(request):
    query = request.GET.get('query', '')
    if query:
        equipments = Equipment.objects.filter(
            Q(id__icontains=query) |
            Q(brand__icontains=query) |
            Q(model__icontains=query) |
            Q(serial_number__icontains=query)
        )
    else:
        equipments = []
    return render(request, 'repairs/search.html', {
        'equipments': equipments,
        'query': query
    })

def about(request):
    return render(request, 'repairs/about.html')

def delete_equipment(request, equipment_id):
    equipment = get_object_or_404(Equipment, id=equipment_id)
    if request.method == 'POST':
        equipment.delete()
        return redirect('search')
    return render(request, 'repairs/delete_confirm.html', {'equipment': equipment})
