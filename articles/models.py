from django.db import models
from tinymce.models import HTMLField
import uuid
from django.utils.text import slugify
from users.models import Profile


# Create your models here.
class Article(models.Model):
    owner = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    body = HTMLField()
    thumbnail = models.ImageField(null=True, blank=True, default='default.jpg')
    categories = models.ManyToManyField('Category', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, editable=False)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def save(self):
        self.slug = slugify(self.title)
        super(Article, self).save()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']

    @property
    def reviewers(self):
        queryset = self.review_set.all().values_list('owner__id', flat=True)
        return queryset

    @property
    def getVoteCount(self):
        reviews = self.review_set.all()
        upVotes = reviews.filter(value='up').count()
        totalVotes = reviews.count()
        ratio = (upVotes / totalVotes) * 100
        self.vote_total = totalVotes
        self.vote_ratio = ratio
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name


class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote')
    )
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    class Meta:
        unique_together = [['owner', 'article']]

    def __str__(self):
        return f'{self.value} --> {self.article}'

    class Meta:
        ordering = ['-created']
