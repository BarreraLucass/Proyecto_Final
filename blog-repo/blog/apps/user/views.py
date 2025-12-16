from django.views.generic import FormView, TemplateView
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

# FORMS
class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

# REGISTER FORM
class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
   
        return cleaned_data

# LOGIN
class AuthLoginView(FormView):
    template_name = "auth/auth-login.html"
    form_class = LoginForm
    success_url = "/"

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]

        user = authenticate(self.request, username=email, password=password)

        if user is not None:
            login(self.request, user)
            return redirect(self.get_success_url())
        else:
            form.add_error(None, "Email o contraseña incorrectos.")
            return self.form_invalid(form)

# REGISTER 
class AuthRegisterView(FormView):
    template_name = "auth/auth-register.html"
    form_class = RegisterForm
    success_url = "/"

    def form_valid(self, form):
        username = form.cleaned_data["username"]
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password1"]

        # Validar email único
        if User.objects.filter(email=email).exists():
            form.add_error("email", "Este email ya está registrado.")
            return self.form_invalid(form)

        # Crear usuario
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # Iniciar sesión automáticamente
        login(self.request, user)

        return redirect(self.get_success_url())


        # Iniciar sesión automáticamente xq si no medio raro q no lo haga
        login(self.request, user)

        return redirect(self.get_success_url())


class UserProfileView(TemplateView):
    template_name = "user/user-profile.html"

class UserUpdateView(TemplateView):
    template_name = "user/user-update.html"