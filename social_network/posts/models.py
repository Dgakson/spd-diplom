from django.db import models
from django.contrib.auth import get_user_model

User  = get_user_model()

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    photo = models.ImageField(upload_to='photos/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']  # автоматическая сортировка по дате создания

    def str(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Like(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='likes')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    ## class Meta позволяет сделать так, чтобы пользователь не мог поставить лайк 2 раза
    class Meta:
        unique_together = ('post', 'author')

    ## Здесь должна быть реализация логики Поставить/удалиить лайк

