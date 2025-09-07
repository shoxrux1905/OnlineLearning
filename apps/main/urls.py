from django.urls import path

from apps.main.views import home_view, course_list_view, specialization_list_view

urlpatterns = [
    path('spec/', specialization_list_view, name='spec'),
    path('course/', course_list_view, name='course'),
    path('home/', home_view, name='home'),
]
