from django.contrib import admin
from .models import QuoraPost, QuoraReply

@admin.register(QuoraPost)
class QuoraPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'user', 'created_at')
    search_fields = ('question', 'user__username')
    list_filter = ('created_at',)

@admin.register(QuoraReply)
class QuoraReplyAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'user', 'created_at', 'total_likes')
    search_fields = ('answer', 'user__username')
    list_filter = ('created_at',)
