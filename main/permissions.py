from functools import wraps
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied


def is_editor(user):
    return user.is_authenticated and user.groups.filter(name="Editor").exists()


def can_edit(user):
    return user.is_authenticated and (user.is_superuser or is_editor(user))


def can_create_delete(user):
    return user.is_authenticated and user.is_superuser


def _role_required(check):
    def decorator(view_func):
        @login_required(login_url="main:login")
        @wraps(view_func)
        def _wrapped(request, *args, **kwargs):
            if not check(request.user):
                raise PermissionDenied   # ini yang bikin error 403
            return view_func(request, *args, **kwargs)
        return _wrapped
    return decorator


editor_required = _role_required(can_edit)
superuser_required = _role_required(can_create_delete)

# ----------------------------- DRF (Tutorial 07) -----------------------------
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsPortfolioOwnerOrReadOnly(BasePermission):
    message = "Only the portfolio owner can change experiences."

    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS
            or request.user.is_superuser
        )


class IsPortfolioOwnerOrEditorOrReadOnly(BasePermission):
    """Baca: semua orang. PUT/PATCH: Editor & pemilik. POST/DELETE: hanya pemilik."""
    message = "Editor hanya dapat mengubah data; menambah dan menghapus hanya untuk pemilik portofolio."

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if not request.user.is_authenticated:
            return False
        if request.user.is_superuser:
            return True
        return (
            request.method in ("PUT", "PATCH")
            and request.user.groups.filter(name="Editor").exists()
        )