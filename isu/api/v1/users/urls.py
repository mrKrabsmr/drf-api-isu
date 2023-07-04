from django.urls import path

from api.v1.users.views import ActivationView, LoginView, RegistrationView


urlpatterns = [
    path("registration/", RegistrationView.as_view()),
    path("login/", LoginView.as_view()),
    path("activate/", ActivationView.as_view(), name="activate")
]