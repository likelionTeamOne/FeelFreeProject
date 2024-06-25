from django.shortcuts import render
from .models import Post, Comment
from .serializers import CommentSerializer
from rest_framework.viewsets import ModelViewSet

# 게시글

# 댓글
class CommentViewSet(ModelViewSet) : 
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self, **kwargs):
        id = self.kwargs['post_id']
        return self.queryset.filter(post=id)
