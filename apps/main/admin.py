from django.contrib import admin

from apps.main.models import CourseModel, SpecializationModel

admin.site.register(CourseModel)
admin.site.register(SpecializationModel)