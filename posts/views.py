from django.shortcuts import render
from rest_framework import generics , permissions
from .serializers import PostSerializer
from .models import Post
from .permissions import IsAuthorOrReadOnly
# Create your views here.


class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    #permission_classes = (permissions.IsAuthenticated,)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAuthorOrReadOnly,)