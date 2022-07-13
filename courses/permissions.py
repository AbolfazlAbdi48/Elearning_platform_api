from rest_framework import permissions


class IsSuperUserOrTeacher(permissions.BasePermission):
    message = 'you must be superuser or teacher.'

    def has_permission(self, request, view):
        return bool(
            request.user.is_authenticated and request.user.is_superuser or
            request.user.is_authenticated and request.user.is_staff
        )
