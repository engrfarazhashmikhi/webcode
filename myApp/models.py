from django.db import models

# Create your models here.

class skill(models.Model):
    language = models.CharField(max_length=255)
    skills = models.CharField(max_length=255)
    
    def __str__(self):
        return self.language
    
    