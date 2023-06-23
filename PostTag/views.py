from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Tag, Category, CategoryPost
from .forms_post import PostForm
from django.shortcuts import render, redirect

def PostTag(request):
    PostTag = Post.objects.order_by('title')
    tags = Tag.objects.all()
    category = Category.objects.all()
    category_post = CategoryPost.objects.all()
    return render(request, "index_post.html", context={"PostTag": PostTag,
                                                  "tags": tags,
                                                  "category": category,
                                                  "category_post": category_post})
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
        return  HttpResponse(f"<f1>Тэга {title} не существует<1/>")
    return  render(request, "posttag.html", context={"posttag": posttag})

def add_post(request):
    if request.method == "GET":
        form = PostForm()
        return render(request, "add_post.html", context={"form": form})
    elif request.method == "POST":
        category_id = request.POST['category']

        category = None
        image = request.FILES.get('image', 'default.jpg')


        if  category_id != '' :
            category = Category.objects.get(id= category_id)






        post = Post.objects.create(title = request.POST['title'],
                            category=category,
                            description=request.POST['description'],
                            image=image,
                            category_post = request.POST['category_post']       )

        posttag = request.POST.getlist('posttag')

        post.posttag.set(posttag)
        post.save()


        return redirect("PostTag")

def search_post(request):
    title = request.GET['title']
    category_post = request.GET['category_post']

    posts = Post.objects.all()


    if title != '':
        print('Фильтруем по названию')
        posts = posts.filter(title__contains=title)
    if category_post != '':
        print('Фильтруем по жанру')
        posts = posts.filter(category_post__title__contains = category_post)




    # search_query = request.GET['genre']
    # books = Book.objects.filter(title__contains=search_query)
    return render(request, 'search_post.html', context={"posts":posts,
                                                        })

def delete_post(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return HttpResponse(f"<h1>Пост с id: {id} удалена!</h1>")
    post.delete()
    return redirect('PostTag')

def update_post(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return HttpResponse(f"<h1>Пост с id: {id} изменена!</h1>")
    if request.method == "GET":
        form = PostForm(instance=post)
        return render(request, "update_post.html", context={"form": form,
                                                            "post": post})
    elif request.method == "POST":
        category_id = request.POST['category']
        category_post_id = request.POST['category_post']

        category = None
        category_post = None
        image = request.FILES.get('image', 'default.jpg')

        if category_id != '':
            category = Category.objects.get(id=category_id)
        if category_post_id != '':
            category_post = CategoryPost.objects.get(id=category_post_id)


        post.title = request.POST['title']
        posttag = request.POST.getlist('posttag')
        post.posttag.set(posttag)
        post.category = category
        post.description = request.POST['description']
        post.category_post = category_post
        post.image = image



        post.save()
        return redirect('/get_posts/', id=post.id)