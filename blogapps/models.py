from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    dept = models.CharField(max_length=100)
    address = models.CharField(max_length=220)
    phone_number = models.CharField(max_length=12)
    
    
    def __str__(self):
        return self.name
    
    