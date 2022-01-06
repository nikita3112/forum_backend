from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = User

    list_display = ('name', 'email')
    ordering = ('email',)

    fieldsets = (
        ('User info', {
            'fields': ('email', 'name',)
        }),
        ('User permissions', {
            'fields': ('is_superuser', 'is_staff', 'is_active', 'groups')
        })
    )

admin.site.register(User, CustomUserAdmin)