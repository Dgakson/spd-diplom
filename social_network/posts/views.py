from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from posts.models import Post, Comment, Like
from posts.permissions import IsAuthenticated, IsPostLikeAuthor
from posts.serializers import PostSerializer, CommentSerializer, LikeSerializer



class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsPostLikeAuthor]
        return [AllowAny()]

    def perform_create(self, serializer):
        """Автоматически назначаем автором поста текущего пользователя"""
        serializer.save(author=self.request.user)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]  # Действия требуют авторизации

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_pk'))
        serializer.save(author=self.request.user, post=post)

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        elif self.action in ['update', 'destroy']:
            return [IsAuthenticated(), IsPostLikeAuthor()]
        return [AllowAny()]

class LikeViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        elif self.action == 'destroy':
            return [IsAuthenticated(), IsPostLikeAuthor()]
        return [AllowAny()]


    ## Здесь должна быть реализация логики Поставить/удалиить лайк

