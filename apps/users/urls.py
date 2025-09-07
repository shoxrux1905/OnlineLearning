from django.urls import path

from apps.users.views import user_login_view, user_registration_view

urlpatterns = [
    path("login/", user_login_view, name='login'),
    path("registration/", user_registration_view, name='registration'),
]
