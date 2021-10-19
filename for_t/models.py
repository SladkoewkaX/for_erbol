from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30, blank=True)
    
    