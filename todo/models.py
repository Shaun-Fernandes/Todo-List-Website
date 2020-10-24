from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


PRIORITY_CHOICES = [
    (1, "Low Priority"),
    (2, "Medium Priority"),
    (3, "High Priority"),
]


class Folder(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def no_of_entries(self):
        return self.entry_set.count()


class Entry(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField()
    priority = models.PositiveIntegerField(default=1, choices=PRIORITY_CHOICES)
    completed = models.BooleanField(default=False)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
