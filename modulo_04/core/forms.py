from django import forms
from .models import Tarefa

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['titulo']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o título da tarefa'
            })
        }
