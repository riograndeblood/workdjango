from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    year = models.IntegerField()
    rating = models.IntegerField(default=0)
    publisher = models.CharField(max_length=50, null=True)
    genre = models.ForeignKey("Genre", on_delete=models.DO_NOTHING, null=True, blank=True, related_name="books")

    def __str__(self):
        return f"книга:{self.id}, Название:{self.title}, автор:{self.author}"

class Genre(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return f"Жанр: {self.id}, {self.title}"

class Movie(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    year = models.IntegerField()
    raiting = models.IntegerField(default=0)

    category = models.ForeignKey("Category", on_delete=models.DO_NOTHING, null=True, blank=True, related_name="movies")
    def __str__(self):
        return f"Фильм:{self.id}, Название:{self.title}, Год:{self.year}"


class Category(models.Model):
    category = models.CharField(max_length=50)
    def __str__(self):
        return f"Категория:{self.id}, {self.category}"