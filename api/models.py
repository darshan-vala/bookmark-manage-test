from django.db import models

# Create your models here.
class Bookmark(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    priority = models.IntegerField(default=3, help_text="Priority from 1 (High) to 5 (Low)")

    def __str__(self):
        return self.title