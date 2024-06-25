from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class UserProfile(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    username = models.CharField(max_length=150, unique=True, default="")
   

    def __str__(self):
        return self.username

class Task(models.Model):
    TASK_STATUS = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    )

    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    assigned_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='assigned_tasks', on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tasks', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=TASK_STATUS, default='pending')

    def __str__(self):
        return self.name
