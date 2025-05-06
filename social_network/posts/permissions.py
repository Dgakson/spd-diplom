from rest_framework import permissions

class IsAuthenticated(permissions.BasePermission):
    """Проверяет, что пользователь авторизован (имеет токен)"""
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

class IsPostLikeAuthor(permissions.BasePermission):
    """Проверяет, что пользователь является автором поста, комментария или лайка"""
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user

# class IsLikeAuthor(permissions.BasePermission):
#     """Проверяет, что пользователь является автором лайка"""
#     def has_object_permission(self, request, view, obj):
#         return obj.user == request.user