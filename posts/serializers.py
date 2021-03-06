from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Post, User
from django.contrib.auth import get_user_model

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'title', 'body', 'created_at',)
        model = Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id' , 'username',)
        model = get_user_model()