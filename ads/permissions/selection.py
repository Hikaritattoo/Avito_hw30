from rest_framework import permissions


class Favorites(permissions.BasePermission):
    massage = 'Only user who added this post can delete it'

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
