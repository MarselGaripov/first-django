from django.db import models
from django.db.models import IntegerField


class Review(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    text = models.TextField()
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name
