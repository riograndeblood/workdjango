from django.db import models
class Tag(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return f"Тэг : {self.title}"

class Book(models.Model):

    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    year = models.IntegerField()
    rating = models.IntegerField(default=0, null=True, blank=True)
    publisher = models.OneToOneField("Publisher", on_delete=models.DO_NOTHING, default=None, null=True, blank=True)
    genre = models.ForeignKey("Genre", on_delete=models.DO_NOTHING, null=True, blank=True, related_name="books")
    tags = models.ManyToManyField("Tag", related_name="books",null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.jpg')
    def __str__(self):
        return f"книга:{self.id}, Название: {self.title}, автор: {self.author}"

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

class Publisher(models.Model):
    LANGUAGES = (
        ("ru","Russian"),
        ("en","English"),
        ("fr","French")
    )
    title = models.CharField(max_length=50)
    languages = models.CharField(max_length=2, choices=LANGUAGES)
    def __str__(self):
        return f"Издание: {self.title} {self.languages}"

    class Meta:
        verbose_name = "Изданиe"
        verbose_name_plural = "Издания"