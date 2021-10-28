from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass

class Tag(models.Model):
    tag = models.CharField(max_length=25)

class Snippet(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="snippets", blank=True)
    author = models.ForeignKey(CustomUser, related_name="snippets", on_delete=models.CASCADE)

    def __str__(self):
        return(f"{self.title}, {self.text}, {self.tags}, {self.author}")


