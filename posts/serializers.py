from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Post, User

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'title', 'body', 'created_at',)
        model = Post
