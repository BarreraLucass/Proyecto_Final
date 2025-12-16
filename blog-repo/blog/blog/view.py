from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class UserprofileView(TemplateView):
    template_name = 'user/user-profile.html'

class AuthLoginView(TemplateView):
    template_name = 'auth/auth-login.html'

class AuthRegisterView(TemplateView):
    template_name ='auth/auth-register.html'

