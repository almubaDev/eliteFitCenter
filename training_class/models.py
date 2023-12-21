from django.db import models
from profile_manager.models import Instructor

class TrainingClass(models.Model):
    name_class = models.CharField(
        max_length=50, 
        null=False, 
        blank=False
    )
    description = models.TextField()
    instructor = models.ForeignKey(
        Instructor,
        on_delete=models.CASCADE
    )