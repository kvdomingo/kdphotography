from django.db import models
from django.utils.timezone import now
from datetime import datetime


class Inquiry(models.Model):
    date_added = models.DateTimeField(default=now, editable=False)
    name = models.CharField(max_length=64)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"({self.date_added}) From {self.name} ({self.email}): {self.message}"

    def __repr__(self):
        return f"<({self.date_added}) {self.name} ({self.email}): {self.message}>"


class Booking(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    point_person = models.CharField(max_length=64)
    email = models.EmailField()
    contact_number = models.BigIntegerField()
    book_date = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()
    purpose = models.CharField(max_length=255)
    details = models.TextField()

    def __str__(self):
        date_parse = self.book_date.strftime("%a %d %b %Y")
        start_parse = self.time_start.strftime("%H%M")
        end_parse = self.time_end.strftime("%H%MH")
        return f"{date_parse} {start_parse}-{end_parse} {self.point_person} ({self.email}, {self.contact_number}): {self.purpose.upper()}"

    def __repr__(self):
        return f"<{date_parse} {start_parse}-{end_parse} {self.point_person} ({self.email}, {self.contact_number}): {self.purpose.upper()}>"
