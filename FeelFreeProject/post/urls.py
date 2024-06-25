from rest_framework.routers import SimpleRouter 
from django.urls import path, include
from .views import CommentViewSet

# 게시글 router

# 댓글
comment_router = SimpleRouter(trailing_slash=False)
comment_router.register('comments', CommentViewSet, basename='comment')


urlpatterns = [
    path('post/<int:post_id', include(comment_router.urls))
]