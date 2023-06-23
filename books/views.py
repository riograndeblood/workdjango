from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Genre, Publisher, Tag
from .forms import BookForm
from django.shortcuts import render, redirect
# модели многие ко многим
# choices, поля
# отобразить все записи в  таблице
# получение всех тэгов в виде йди названии книги

def books(request):
    books = Book.objects.all()
    genres = Genre.objects.all()
    publishers = Publisher.objects.all()
    return render(request, "index_book.html", context={"books": books,
                                                  "genres": genres,
                                                  "publisher": publishers})


def get_book(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return HttpResponse(f"<h1>Такой книги не существует{id}</h1>")
    return  render(request, "detail_book.html", context={"book": book})

def get_genre_books(request, title):
    try:
        genre = Genre.objects.get(title=title)
    except Genre.DoesNotExit:
        return  HttpResponse(f"<f1>Жанра с названием : {title} не сужествует<1/>")
    return  render(request, "genre.html", context={"genre": genre})

def get_tag_books(request, title):
    try:
        tag = Tag.objects.get(title=title)
    except Tag.DoesNotExit:
        return  HttpResponse(f"<f1>Тэга с названием : {title} не сужествует<1/>")

    print("Все книги у тега")
    tag_books = tag.books.all()
    return  render(request, "tag_detail.html", context={"tag_books": tag_books,
                                                        "tag": tag})

def add_book(request):
    if request.method == "GET":
        form = BookForm()
        return render(request, "add_book.html", context={"form": form})
    elif request.method == "POST":
        publisher_id = request.POST['publisher']
        genre_id = request.POST['genre']

        publisher = None
        genre = None
        image = request.FILES.get('image', 'default.jpg')

        if publisher_id != '':
            publisher = Publisher.objects.get(id=publisher_id)
        if genre_id != '':
            genre=Genre.objects.get(id=genre_id)






        book = Book.objects.create(title = request.POST['title'],
                            author = request.POST['author'],
                            year=request.POST['year'],
                            rating=request.POST['rating'],
                            publisher=publisher,
                            genre=genre,
                            image=image)

        tags = request.POST.getlist('tags')
        book.tags.set(tags)
        book.save()

        return redirect("books")


def search_book(request):
    title = request.GET['title']
    genre = request.GET['genre']
    books = Book.objects.all()


    if title != '':
        print('Фильтруем по названию')
        books = books.filter(title__contains=title)

    if genre != '':
        print('Фильтруем по жанру')
        books = books.filter(genre__title__contains = genre)
    print(books)

    # search_query = request.GET['genre']
    # books = Book.objects.filter(title__contains=search_query)
    return render(request, 'search_book.html', context={"books":books,
                                                        })
def delete_book(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return HttpResponse(f"<h1>Книга с id: {id} удалена!</h1>")
    book.delete()
    return redirect('books')
def update_book(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return HttpResponse(f"<h1>Книга с id: {id} изменена!</h1>")
    if request.method == 'GET':
        form = BookForm(instance=book)
        return render(request, 'update_book.html', context={'form':form,
                                                            'book':book})
    else:
        publisher_id = request.POST['publisher']
        genre_id = request.POST['genre']

        publisher = None
        genre = None
        image = request.FILES.get('image', "default.jpg")

        if publisher_id != '':
            publisher = Publisher.objects.get(id=publisher_id)

        if genre_id != '':
            genre = Genre.objects.get(id=genre_id)

        book.title = request.POST['title']
        book.author = request.POST['author']
        book.year = request.POST['year']
        book.rating = request.POST['rating']
        book.publisher = publisher
        book.genre = genre
        book.image = image
        tags = request.POST.getlist('tags')
        book.tags.set(tags)

        book.save()
        return redirect('/get_books/', id=book.id)


