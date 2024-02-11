from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Trip(models.Model):
    title = models.CharField(max_length=200)
    picture = models.URLField(blank=True)
    description = models.TimeField()
    location = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_At = models.DateTimeField(auto_no_add=True)

    def __str__(self):
        return self.title
