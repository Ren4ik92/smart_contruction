from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class PostNews(models.Model):
    heading = models.CharField(max_length=50, default="")
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    image = models.ImageField(unique=True, blank=True)

    def __str__(self):
        return self.text
