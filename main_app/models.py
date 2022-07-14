from django.db import models
from django.urls import reverse

# Create your models here.

#USER IMPORT
from django.contrib.auth.models import User

# Add the MUSIC class & list and view function below the imports
class Music(models.Model):
  name = models.CharField(max_length=100)
  picture = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  youtube = models.CharField(max_length=100)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
 

  def __str__(self):
    return self.name

  # Add this method
  def get_absolute_url(self):
    return reverse('details', kwargs={'music_id': self.id})
