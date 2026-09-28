from main.permissions import can_create_delete, can_edit, is_editor


def user_roles(request):
    return {
        "is_editor": is_editor(request.user),
        "can_edit": can_edit(request.user),
        "can_create_delete": can_create_delete(request.user),
    }