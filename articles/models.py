from django.db import models
from tinymce.models import HTMLField
import uuid
from django.utils.text import slugify


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    body = HTMLField()
    thumbnail = models.ImageField(null=True, blank=True, default='default.jpg')
    categories = models.ManyToManyField('Category', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def save(self):
        self.slug = slugify(self.title)
        super(Article, self).save()

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name