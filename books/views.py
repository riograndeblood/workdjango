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
    return render(request, "index.html", context={"books": books,
                                                  "genres": genres,
                                                  "publisher": publishers})
