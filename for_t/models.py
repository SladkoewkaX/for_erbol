from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.surname}, {self.name}'