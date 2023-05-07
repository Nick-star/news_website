from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
