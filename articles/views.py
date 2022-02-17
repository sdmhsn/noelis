from django.shortcuts import render
from .models import Article, Category
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# from django.db.models import Count


def articles(request):
    articles = Article.objects.all()
    categories = Category.objects.all()

    context = {
        'title': 'Articles - NOELIS Author Blog',
        'articles': articles,
        'categories': categories,
    }

    return render(request, 'articles/articles.html', context)


def categoryView(request, cats):
    categories = Category.objects.all()
    # categories2 = Category.objects.all().annotate(posts_count=Count('name'))
    queryset = Article.objects.filter(categories__name__contains=cats).order_by('-id')

    # for i in categories:
    #     print(i)
    
    # q = Category.objects.aggregate(Count('name'))
    # print(q)

    # print(categories)

    for category in categories:
        print(category.article_set.count())

    paginator = Paginator(queryset, 5)
    pagez2 = request.GET.get('page')

    try:
        paginated_queryset = paginator.page(pagez2)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'cats': cats,
        'categories': categories,
        'queryset': paginated_queryset,  # digunakan oleh blog post dan pagination. harus disatukan agar pagination bekerja.
        # 'page_request_var': page_request_var,
    }

    return render(request, 'articles/articles.html', context)


def article(request):
    articles = Article.objects.all()

    context = {
        'title': Article.objects.all()[0],
        'articles': articles,
    }

    return render(request, 'articles/single-article.html', context)

