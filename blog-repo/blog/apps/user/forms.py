from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import FileInput
from .models import User



class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {
                "placeholder": "Usuario o Email",
                "autofocus": True,
            }
        )
        self.fields["password"].widget.attrs.update(
            {"placeholder": "Contraseña"}
        )


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "alias", "nombre", "")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

        placeholders = {
            "username": "Ej: luchardox",
            "email": "lucas@legendofleague.com",
            "alias": "Gatomachi",
            "nombre": "Naylux",
            "password": "Mínimo 8 caracteres",            
        }

        for name, text in placeholders.items():
            self.fields[name].widget.attrs["placeholder"] = text

        self.fields["username"].widget.attrs["autofocus"] = True


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "nombre",
            "alias",
            "email",
            "avatar",
        ]
        labels = {
            "nombre": "Nombres",
            "alias": "Apellidos",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["avatar"].widget = FileInput(
            attrs={"class": "hidden js-file-input", "id": "id_avatar"}
        )