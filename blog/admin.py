from django.contrib import admin
from blog.models import Post, Tag, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    raw_id_fields = ['author', 'likes', 'tags']
    pass


class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)
    pass


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'published_at')
    raw_id_fields = ['author']
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
