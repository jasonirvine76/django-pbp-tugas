from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    date = models.DateField()
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    is_finished = models.BooleanField(default=False)
