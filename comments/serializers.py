from rest_framework import serializers
from rest_framework.utils import field_mapping 
from .models import Post, Comment

class PostSer(serializers.ModelSerializer):
    class Meta:
        fields = ('author', 'title', 'body',)
        model = Post

class CommentsSer(serializers.ModelSerializer):
    class Meta:
        fields = ('post', 'name', 'body', 'reply',)
        model = Comment