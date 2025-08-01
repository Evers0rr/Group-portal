def is_admin_or_moderator(user):
    return user.is_superuser or user.is_staff
