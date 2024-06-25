from django.db import models
from django.contrib.auth.models import User

# 게시글 모델
class Post(models.Model) : 
    title = models.CharField(verbose_name="제목", max_length=128)

    def __str__(self):
        return self.title

# 댓글 모델
class Comment(models.Model) :
    comment = models.CharField(verbose_name="댓글", max_length=128)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self) :
        return self.comment
