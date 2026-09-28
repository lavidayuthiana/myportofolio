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