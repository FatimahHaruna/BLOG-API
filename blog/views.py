from rest_framework import viewsets
from django.shortcuts import render
from .models import BlogPost 
from .serializers import BlogPostSerializer

# Create your views here.
class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all() #tells django what data this view will work with
    serializer_class = BlogPostSerializer #tells the view which serializer to use to convert the data
    
