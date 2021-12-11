from django.contrib import admin
from .Models.m_post import Tag,Post
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    # displaying posts with title slug and created time
    list_display = ('title', 'slug',)
    list_filter = ("title",)
    search_fields = ['title', 'content']
    # prepopulating slug from title
    prepopulated_fields = {'slug': ('title', )}
    summernote_fields = ('content', )
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Tag,TagAdmin)
admin.site.register(Post,PostAdmin)