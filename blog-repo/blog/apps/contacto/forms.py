from django import forms
from .models import MensajeContacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = MensajeContacto
        fields = ['nombre', 'email', 'asunto', 'mensaje']

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'input'}),
            'email': forms.EmailInput(attrs={'class': 'input'}),
            'asunto': forms.TextInput(attrs={'class': 'input'}),
            'mensaje': forms.Textarea(attrs={'class': 'input h-32'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if MensajeContacto.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya ha sido utilizado para enviar un mensaje. Espere por nuestra respuesta, por favor.")
        return email
    
    def clean_mensaje(self):
        mensaje = self.cleaned_data.get('mensaje')
        if len(mensaje) < 10:
            raise forms.ValidationError("El mensaje es demasiado corto. Por favor, proporcione más detalles para poder ayudarlo mejor.")
        return mensaje
    
    def save(self, commit=True):
        mensaje_contacto = super().save(commit=False)
        if commit:
            mensaje_contacto.save()
        return mensaje_contacto