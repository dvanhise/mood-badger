from django.db import models
from django.contrib.auth.models import User


class Mood(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, blank=False)
    streak = models.IntegerField()
    date = models.DateField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.description
