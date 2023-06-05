from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Tag, Category


def PostTag(request):
    PostTag = Post.objects.all()
    tags = Tag.objects.all()
    category = Category.objects.all()
    return render(request, "index_post.html", context={"PostTag": PostTag,
                                                  "tags": tags,
                                                  "category": category})
def get_post(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return HttpResponse(f"<h1>Такого поста не существует{id}</h1>")
    return  render(request, "detail_post.html", context={"post": post})

def get_posttag_posts(request, title):
    try:
        posttag = Tag.objects.get(title=title)
    except Tag.DoesNotExit:
        return  HttpResponse(f"<f1>Тэга {title}не существует<1/>")
    return  render(request, "posttag.html", context={"posttag": posttag})






