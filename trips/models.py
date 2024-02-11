from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Trip(models.Model):
    title = models.CharField(max_length=200)
    picture = models.URLField(blank=True)
    description = models.TextField()
    location = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    future_trip = models.BooleanField(default=False)
    past_trip = models.BooleanField(default=False)



    def __str__(self):
        return self.title
