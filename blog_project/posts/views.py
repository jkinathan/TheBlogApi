from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import PostSerializer
from .models import Post

# Create your views here.

class PostList(generics.ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticated,) #view level Permissions
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer