from django.db import models

# Create your models here.

class Comment(models.Model):
  character_id = models.IntegerField(primary_key=True)
  comment = models.TextField()
  updated_date = models.DateTimeField(auto_now=True)

class Fav(models.Model):
  character_id = models.IntegerField(primary_key=True)
  updated_date = models.DateTimeField(auto_now=True)
