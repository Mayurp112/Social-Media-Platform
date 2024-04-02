from django.contrib import admin
from .models import User, Post, Comment, Notification, Message

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'name']
    search_fields = ['username', 'email', 'name']
    filter_horizontal = ['following']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'text', 'image', 'video', 'created_at']
    search_fields = ['user__username', 'text']
    list_filter = ['created_at']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'text', 'created_at']
    search_fields = ['user__username', 'post__text', 'text']
    list_filter = ['created_at']

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'message', 'read', 'created_at']
    search_fields = ['user__username', 'message']
    list_filter = ['read', 'created_at']

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['sender', 'receiver', 'message', 'timestamp', 'read']
    search_fields = ['sender__username', 'receiver__username', 'message']
    list_filter = ['timestamp', 'read']
