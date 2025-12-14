from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['usuario', 'articulo', 'contenido', 'activo']
        widgets = {
            'contenido': forms.Textarea(attrs={'rows': 3, 'cols': 40, "placeholder": "Escribe tu comentario aquí..."}),
        } # Personaliza el widget del campo 'contenido'