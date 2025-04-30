from django import forms
from .models import Equipment

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = '__all__'
        widgets = {
            'entry_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'exit_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'defect_description': forms.Textarea(attrs={
                'rows': 4,
                'class': 'form-control'
            }),
            'repair_description': forms.Textarea(attrs={
                'rows': 4,
                'class': 'form-control'
            }),
            'observations': forms.Textarea(attrs={
                'rows': 4,
                'class': 'form-control'
            }),
        } 