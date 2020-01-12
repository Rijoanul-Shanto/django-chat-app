from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user.models import User


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'name', 'date_joined', 'is_active', 'is_staff', 'avatar')
    list_filter = ('email', 'is_staff', 'is_active',)
    # show after create
    fieldsets = (
        (None, {'fields': ('email', 'name', 'date_joined', 'password', 'avatar')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    # show when create
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'is_staff', 'is_active', 'avatar')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, CustomUserAdmin)