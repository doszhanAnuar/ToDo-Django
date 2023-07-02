from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=200)
    discription = models.TextField(blank=True)
    date = models.DateTimeField(blank=False)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    def __str__(self):
        return self.name
