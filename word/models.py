from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Word(models.Model):
    word_id=models.IntegerField(primary_key=True)
    word_spell=models.CharField(max_length=20)
    word_mean=models.CharField(max_length=20)
    word_update_date = models.DateTimeField(default=timezone.now)
    u_id = models.ForeignKey(User, on_delete=models.CASCADE)
