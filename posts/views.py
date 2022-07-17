from django.shortcuts import render
from rest_framework import generics , permissions
from .serializers import PostSerializer , UserSerializer
from .models import Post
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model

# Create your views here.


class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    #permission_classes = (permissions.IsAuthenticated,)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAuthorOrReadOnly,)
    
class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()