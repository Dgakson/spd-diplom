from rest_framework import serializers
from posts.models import Comment, Post, Like
from django.contrib.auth.models import User

### Решил не использовать, а просто переопределил поле User
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username']

class CommentSerializer(serializers.ModelSerializer):
    # author = UserSerializer(read_only=True)
    # переопределил поле User. Вместо id получаю username
    author = serializers.CharField(source='author.username')

    class Meta:
        model = Comment
        fields = '__all__'


        read_only_fields = ('author', 'created_at', 'updated_at')


class LikeSerializer(serializers.ModelSerializer):
    # author = UserSerializer(read_only=True)
    author = serializers.CharField(source='author.username')

    class Meta:
        model = Like
        fields = '__all__'
        read_only_fields = ('author', 'created_at')


class PostSerializer(serializers.ModelSerializer):
    # author = UserSerializer(read_only=True)
    author = serializers.CharField(source='author.username')
    comments = CommentSerializer(many=True, read_only=True)
    # likes = LikeSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()  # метод определен ниже

    class Meta:
        model = Post
        fields = ['id','author','description','photo','created_at','updated_at',
                  'photo','comments','likes_count']
        read_only_fields = ('author', 'created_at', 'updated_at')

    def get_likes_count(self, obj):
        return obj.likes.count()
