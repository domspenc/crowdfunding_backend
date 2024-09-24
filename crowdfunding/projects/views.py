from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Project, Pledge
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer


#https://github.com/SheCodesAus/PlusLessonContent/blob/main/3_Django_and_DRF/views/views.md#5----adding-some-more-functionality-to-our-view-
class ProjectList(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )
        return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )

class ProjectDetail(APIView):
  def get_object(self, pk):
      try:
          project = Project.objects.get(pk=pk)
          return project
      except Project.DoesNotExist:
          raise Http404
  def get(self, request, pk):
      project = self.get_object(pk)
      serializer = ProjectDetailSerializer(project)
      return Response(serializer.data)

class PledgeList(APIView):
  def get(self, request):
      pledges = Pledge.objects.all()
      serializer = PledgeSerializer(pledges, many=True)
      return Response(serializer.data)
  def post(self, request):
      serializer = PledgeSerializer(data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(
              serializer.data,
              status=status.HTTP_201_CREATED
          )
      return Response(
          serializer.errors,
          status=status.HTTP_400_BAD_REQUEST
      )



# # You can either use a class or a function to create views in Django

# # 'index' is the function name used to label the default page in an app
# # The below are FBVS (function-based views)
# # Eg: 
# def index(request):
#     return render(request, 'index.html')
# # The above code is doing the following things:
# # The index function takes in a 'request' object as the argument (this is all the information from the user),
# # then we return back the results of the 'render' command, which takes two parameters; our 'request' and the name of the html file (index.html)

# # You create different views for the different pages on your site, for example:
# def about(request):
#     return render(request, 'about.html')

# # The html file it's going to display is known (in Django terms) as a 'template', which will be static, but we can make dynamic!
# # You would start by creating a templates folder within the 'projects' folder, which will hold the html templates (but maybe wait to do this in class!)

# # Routing (Wiring up Views)
# # Tells the web framework "Hey, if a user goes to this particular url or performs this particular action, *this* is now the code that I want you to excecute in response to this"
# # The way that django does this is by using a urlConf file 
# # This is a collection of paths (or routes on other web frameworks!) that are saying ("Hey, when a user goes to this path, this is where I want you to send that request")

# # The global file for this is inside the project settings folder ('crowdfunding'), inside the urls.py file
# # urlpatterns is the global variable for this entire project
# # we use this url.py file to tell djang o where all of our urlConfs are set up so it knows wat to do

# # inside the app settings folder ('projects') you can add a url.py file that will be specific to the app (not global)
# # here, i need to import a library so i can start setting up my paths
# # you import it using [ from django.urls import path ]
# # then you create the urlpatterns list (this list is our urlConf!):
# # each path will look for 2 things:
# # 1. the route (this indicates where the user is going inside our application; this can be left blank indicating a default path)
# # 2. code that points to the function we want to call (located inside our views.py file!)
# # so the working code will look like this:
# urlpatterns = [
#     path('', views.index, name='index')
# ]
# # you can also give it a name, which is the final parameter above. This is super helpful to prevent having to hardcode in a path, you can just look it up using the name!
# # you can add all of your paths to your urlConf, eg:
# urlpatterns = [
#     path('', views.index, name='index')
#     path('about', views.about, name='about')
# ]

# # Now, we need to register this information globally, so we go back into the project settings folder ('crowdfunding'), then into the existing urls.py file, and we add the new paths in
# # we do this by importing one more library called 'include'
# # this can be added to the end of the [ from django.urls import path, include ] line at the top of the file
# # 'include' will allow us to add the urlConf from the app into the global crowdfunding url.py file
# # we do this with one line of code:
# path('', include('projects.urls'))
