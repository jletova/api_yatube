from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    messgage = "Редактирование чужого контента запрещено"

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
