from django.db import models


class Article(models.Model):
    version = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)
    text = models.TextField()
    article_id = models.IntegerField()
    flag_default = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
