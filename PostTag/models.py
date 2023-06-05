from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    posttag = models.ManyToManyField("Tag", related_name="posts")
    category = models.OneToOneField("Category", on_delete=models.DO_NOTHING, default=None)
    description = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Пост: {self.id}, Название: {self.title}, Описание: {self.description}"


    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

class Tag(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"Тэги: {self.title}"

class Category(models.Model):
    LANGUAGES = (
        ("ru","Russian"),
        ("en","English"),
        ("fr","French")
    )
    title = models.CharField(max_length=50)
    languages = models.CharField(max_length=2, choices=LANGUAGES, default=None)
    def __str__(self):
        return f"Канал: {self.title}.{self.languages}"


