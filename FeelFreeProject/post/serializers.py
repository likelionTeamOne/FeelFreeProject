from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Post, Comment
from django.contrib.auth.models import User

# 게시물

# 댓글
class CommentSerializer(ModelSerializer) : 
    writer = serializers.ReadOnlyField(source = 'writer.username')

    class Meta:
        model = Comment
        fields = ['id', 'comment', 'post', 'writer']