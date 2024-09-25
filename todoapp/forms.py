from django import forms
from .models import Task

class TaskManageForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M'],
        widget=forms.DateTimeInput(attrs={
            'type': 'datetime-local',
            'class': 'form-control',  # CSS-клас
        })
    )

    class Meta:
        model = Task
        fields = ['title', 'deadline']
