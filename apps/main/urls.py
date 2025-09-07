from django.urls import path

from apps.main.views.Course import course_list_view
from apps.main.views.Specialization import specialization_list_view

urlpatterns = [
    path('spec/', specialization_list_view, name='spec'),
    path('course/', course_list_view, name='course'),
]
