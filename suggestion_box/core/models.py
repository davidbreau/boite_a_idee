from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    birth_date = models.DateField(auto_now=False, null=True)
    
class Suggestion(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=300, null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    
class Vote(models.Model):
    suggestion = models.ForeignKey(Suggestion, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    type_vote = models.BooleanField()
    