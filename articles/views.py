from django.shortcuts import render
from .models import Article, Category
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


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
    articles = Article.objects.all()
    categories = Category.objects.all()
    # categories2 = Category.objects.all().annotate(posts_count=Count('name'))
    queryset = Article.objects.filter(categories__name__contains=cats).order_by('-id')

    # for i in categories:
    #     print(i)
    
    # q = Category.objects.aggregate(Count('name'))
    # print(q)

    # print(categories)

    # for category in categories:
    #     print(category.article_set.count())

    paginator = Paginator(queryset, 5)
    pagez2 = request.GET.get('page')

    try:
        paginated_queryset = paginator.page(pagez2)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'title': 'Article Categories - NOELIS Author Blog',
        'cats': cats,
        'categories': categories,
        'articles': articles,
        'queryset': paginated_queryset,
        # 'page_request_var': page_request_var,
    }

    return render(request, 'articles/articles.html', context)


def article(request, slugInput):
    articleObj = Article.objects.get(slug=slugInput)
    print(articleObj)

    context = {
        'title': f'{articleObj} - NOELIS Author Blog',
        'article': articleObj,
    }

    return render(request, 'articles/single-article.html', context)

