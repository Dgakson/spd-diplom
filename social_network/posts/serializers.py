from rest_framework import serializers
from posts.models import Comment, Post
from django.contrib.auth.models import User

# Решил не использовать, а просто переопределил поле User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class CommentSerializer(serializers.ModelSerializer):
    # переопределил поле User. Вместо id получаю username
    user = serializers.CharField(source='user.username')

    class Meta:
        model = Comment
        fields = ['user', 'text', 'created_at']
        read_only_fields = ['author']


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    # переопределил поле User. Вместо id получаю username
    user = serializers.CharField(source='user.username')

    class Meta:
        model = Post
        fields = ['id', 'description', 'photo', 'user','created_at', 'comments']

    # def to_representation(self, post):
    #     """ Метод вывода количества лайков в посте """
    #     representation = super().to_representation(post)
    #     representation['likes_count'] = post.likes.count()
    #     return representation