from django.shortcuts import render
from rest_framework import generics , permissions , viewsets
from .serializers import PostSerializer , UserSerializer
from .models import Post
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model

# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
