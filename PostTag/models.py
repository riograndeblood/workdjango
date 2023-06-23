from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    posttag = models.ManyToManyField("Tag", related_name="posts",blank=True)
    category = models.OneToOneField("Category", on_delete=models.DO_NOTHING, default=None, null=True, blank=True)
    description = models.TextField(max_length=500,default=None, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    category_post = models.ForeignKey("CategoryPost", on_delete=models.DO_NOTHING, null=True, blank=True, related_name="PostTag")
    image = models.ImageField(default='default.jpg')

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
    languages = models.CharField(max_length=2, choices=LANGUAGES)
    def __str__(self):
        return f"Канал: {self.title}.{self.languages}"


class CategoryPost(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return f"Категория: {self.id}, {self.title}"
