from rest_framework.serializers import ModelSerializer
from .models import Post, Comment

# 게시물

# 댓글
class CommentSerializer(ModelSerializer) : 
    class Meta:
        model = Comment
        fields = ['id', 'comment', 'post']