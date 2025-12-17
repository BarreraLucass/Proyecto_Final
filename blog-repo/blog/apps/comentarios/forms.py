from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']  # Solo mostramos el campo de texto
        widgets = {
            'contenido': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Escribe tu comentario aquí...',
                'class': 'form-control'
            }),
        }
        labels = {
            'contenido': ''
        }