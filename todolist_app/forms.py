from django import forms
from django import forms
from .models import TaskList


class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = ['task', 'done']
