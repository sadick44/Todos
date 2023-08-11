from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    status = (
        ("Pending", "Pending"),
        ("Success", "success"),
        ("Failed", "Failed")
    )

    title = models.CharField(max_length=20)
    status = models.CharField(choices=status, max_length=25)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)