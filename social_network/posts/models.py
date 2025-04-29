from django.db import models
from django.contrib.auth import get_user_model

User  = get_user_model()

class Post(models.Model):
    description = models.TextField()
    photo = models.ImageField(upload_to='photos/')
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # claass Meta позволяет сделать так, чтобы пользователь не мог поставить лайк 2 раза
    class Meta:
        unique_together = ('post', 'user')