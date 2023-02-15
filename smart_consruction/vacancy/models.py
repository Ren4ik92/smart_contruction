from django.db import models


class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    date_expired = models.DateTimeField()
    is_archived = models.BooleanField(default=False)

    def archive(self):
        self.is_archived = True
        self.save()
