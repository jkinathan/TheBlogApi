from django.shortcuts import render
from rest_framework import generics, permissions
from .permissions import IsAuthorOrReadOnly # new
from .serializers import PostSerializer, UserSerializer #new
from django.contrib.auth import get_user_model #new
from .models import Post
from rest_framework import viewsets # new

# Create your views here.

# class PostList(generics.ListCreateAPIView):
#     #permission_classes = (permissions.IsAuthenticated,) #view level Permissions
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     #permission_classes = (permissions.IsAuthenticated,)
#     permission_classes = (IsAuthorOrReadOnly,)#custom permissions for rest_framework API
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class UserList(generics.ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
    
# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
    
class PostViewSet(viewsets.ModelViewSet): # new
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
class UserViewSet(viewsets.ModelViewSet): # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer