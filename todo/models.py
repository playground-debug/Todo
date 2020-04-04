from django.db import models
from django.contrib.auth.forms import User


class Todo(models.Model):
    task = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    time = models.DateTimeField(auto_now_add=True)
    complete = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.task
