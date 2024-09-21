from rest_framework import serializers
from django.apps import apps

class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
      model = apps.get_model('projects.Project')
      fields = '__all__'


# This starts the shell...
# Remember - you need to be in the correct folder so it can locate the manage.py file using the below code
# Eg: if you're already inside the 'crowdfunding' folder, you can remove it from the path within the command!
python crowdfunding/manage.py shell

# This line imports the existing models (tables) from our Project class, inside the projects.models.py file
from projects.models import Project

# This line imports the serializers module from Django (located in the projects.serializers.py file)
# The ProjectSerializer class tells Django what to do (using the Meta class) when we make the call to seralize our models 
from projects.serializers import ProjectSerializer


# This line saves all the objects within our models to the variable 'record_list', to be used later...
record_list = Project.objects.all()


# This line calls the ProjectSerializer class and uses it on the data saved in 'record_list' 
# It then saves the serialized data inside the 'my_serializer' variable
# We use the many=True keyword argument to warn it that this is a list of records instead of just a single instance!
my_serializer = ProjectSerializer(record_list, many=True)

# Prints the output - a list of JSON distionaries containing our serialized data!
print(my_serializer.data)
