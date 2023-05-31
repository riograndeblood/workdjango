from django.shortcuts import render
from .models import Post, Tag, Category
def PostTag(request):
    PostTag = Post.objects.all()
    tags = Tag.objects.all()
    category = Category.objects.all()
    return render(request, "index.html", context={"PostTag": PostTag,
                                                  "tags": tags,
                                                  "category": category})







