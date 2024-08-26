from django.db import models

# Create your models here.

class students(models.Model):
    firstname=models.CharField(max_length=120)
    lastname=models.CharField(max_length=120)
    """ python manage.py makemigrations """
