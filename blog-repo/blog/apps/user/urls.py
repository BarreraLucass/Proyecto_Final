from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

app_name = "user"

urlpatterns = [
    # AUTH SYSTEM
    path("login/", AuthLoginView.as_view(), name="login"),
    path("register/", AuthRegisterView.as_view(), name="register"),

    # LOGOUT
    path('logout/', LogoutView.as_view(), name='logout'),


    # USER PROFILE
    path("user/profile/", UserProfileView.as_view(), name="user-profile"),
    path("user/profile/edit/", UserUpdateView.as_view(), name="user-update"),
]