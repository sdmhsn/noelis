from django.contrib import admin
from .models import Article, Category, Review


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Review)
