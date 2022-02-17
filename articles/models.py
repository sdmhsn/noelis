from django.db import models
from tinymce.models import HTMLField
import uuid


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    body = HTMLField()
    thumbnail = models.ImageField(null=True, blank=True, default='default.jpg')
    categories = models.ManyToManyField('Category', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name