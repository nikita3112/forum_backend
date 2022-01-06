from django.contrib import admin
from .models import Message, Thread, Theme

# Register your models here.
@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    pass

@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    pass

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass
