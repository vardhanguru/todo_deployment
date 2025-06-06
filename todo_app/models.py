from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):


    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=30)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task
