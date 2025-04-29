from django.shortcuts import render
from rest_framework import status
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from posts.models import Post, Comment, Like
# from posts.permissions import IsOwnerOrReadOnly
from posts.serializers import PostSerializer, CommentSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # def get_permissions(self):
    #     """ Метод получения прав для действий с объектом пост. """
    #     if self.action in ["create", "update", "partial_update", "destroy"]:
    #         return [IsAuthenticated(), IsOwnerOrReadOnly()]
    #     return [IsOwnerOrReadOnly()]
    #
    # def perform_create(self, serializer):
    #     """
    #     Метод создания поста
    #     для передачи аутентифицированного по токену пользователя
    #     """
    #     serializer.save(author=self.request.user)


