from django.db import models

class SpecializationModel(models.Model):
    name = models.CharField(max_length=50)
    tools = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.ImageField("upload_to")
    
    def __str__(self):
        return self.name

class CourseModel(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    image = models.ImageField("upload_to")
    
    def __str__(self):
        return self.name
    
    
