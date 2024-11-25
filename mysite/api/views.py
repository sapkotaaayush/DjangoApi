from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Blogpost
from .serializers import BlogpostSerializer
# Create your views here.

class BlogPostListCreate(generics.CreateAPIView):
    queryset = Blogpost.objects.all()
    serializer_class = BlogpostSerializer
    
    def delete(self, request, *args, **kwargs):
        Blogpost.objects.all()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
# class BlogPostRetrieveUpdateDestriy(generics.RetrieveUpdateDestroyAPIView):
#      queryset = Blogpost.objects.all()
#      serializer_class = BlogpostSerializer
#      lookup_field = "pk"
    
    