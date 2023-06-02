from django.contrib import admin

from .models import Post, Tag, Category
class PostAdmin(admin.ModelAdmin):
    list_display = ("id","title","category","date", "get_tags")
    def get_tags(self,obj):
        tags = obj.posttag.all()
        return  ",\n".join([t.title for t in tags])
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Category)
