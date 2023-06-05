from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Genre, Publisher

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
    return  render(request, "detail_book.html", context={"book":book})

def get_genre_books(request, title):
    try:
        genre = Genre.objects.get(title=title)
    except Genre.DoesNotExit:
        return  HttpResponse(f"<f1>Жанра не сужествует<1/>")
    return  render(request, "genre.html", context={"genre": genre})


