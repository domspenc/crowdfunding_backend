from django.db import models
from django.contrib.auth import get_user_model

# Create your models here. This translates to a 'table' in the database (according to Atlas!)
class Project(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField()
  goal = models.IntegerField()
  image = models.URLField()
  is_open = models.BooleanField()
  date_created = models.DateTimeField(auto_now_add=True)
  owner = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,
    related_name='owned_projects'
)

class Pledge(models.Model):
  amount = models.IntegerField()
  comment = models.CharField(max_length=200)
  anonymous = models.BooleanField()
  project = models.ForeignKey( # the project variable is the 'name' of the foreign key 'column'!
      'Project', # this line creates the relationship between the Pledge table and the Project table (using the FK)
      on_delete=models.CASCADE, # this ensures if the Project that this table is related to is deleted, to also delete this pledge
      related_name='pledges' # https://github.com/SheCodesAus/PlusLessonContent/blob/main/3_Django_and_DRF/model_relations/model_relations.md#13---%EF%B8%8F-the-related-name-%EF%B8%8F
  )
  supporter = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,
    related_name='pledges'
)

  