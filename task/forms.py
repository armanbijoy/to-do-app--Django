from .models import *
from django import forms

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'