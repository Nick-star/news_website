from django.db import models

class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey('articles.Article', on_delete=models.CASCADE)
    author = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
