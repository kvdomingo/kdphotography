from django.db import models
from django.utils.timezone import now


class Contact(models.Model):
    date_added = models.DateTimeField(default=now, editable=False)
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=32)
    message = models.TextField()

    def __str__(self):
        return f"({self.date_added}) From {self.name} ({self.email}): {self.message}"
