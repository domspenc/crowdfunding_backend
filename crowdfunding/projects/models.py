from django.db import models

# Create your models here. This translates to a 'table' in the database (according to Atlas!)
class Project(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField()
  goal = models.IntegerField()
  image = models.URLField()
  is_open = models.BooleanField()
  date_created = models.DateTimeField(auto_now_add=True)