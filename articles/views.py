from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Article, Category, Review
from .forms import ArticleForm, ReviewForm
from .utils import searchArticles, paginateArticles


def articles(request):
    articles, search_query = searchArticles(request)
    custom_range, articles = paginateArticles(request, articles, 6)
    populars = Article.objects.all().order_by('-vote_ratio')
    categories = Category.objects.all()
    reviews = Review.objects.all()

    context = {
        'title': 'Articles - NOELIS Author Blog',
        'articles': articles,
        'categories': categories,
        'search_query': search_query,
        'custom_range': custom_range,
        'reviews': reviews,
        'populars': populars
    }

    return render(request, 'articles/articles.html', context)


def categoryView(request, categoryInput):
    categories = Category.objects.all()
    articles = Article.objects.filter(categories__name__contains=categoryInput).order_by('-created')
    populars = Article.objects.all().order_by('-vote_total')
    custom_range, articles = paginateArticles(request, articles, 6)
    reviews = Review.objects.all()

    context = {
        'title': 'Article Categories - NOELIS Author Blog',
        'category': categoryInput,
        'articles': articles,
        'populars': populars,
        'categories': categories,
        'custom_range': custom_range,
        'reviews': reviews
    }

    return render(request, 'articles/articles.html', context)


def article(request, slugInput):
    articleObj = Article.objects.get(slug=slugInput)
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.owner = request.user.profile
        review.article = articleObj
        review.save()

        articleObj.getVoteCount
        messages.success(request, 'Review submitted successfully!')
        return redirect('article', slugInput=articleObj.slug)

    context = {
        'title': f'{articleObj} - NOELIS Author Blog',
        'article': articleObj,
        'form': form
    }

    return render(request, 'articles/single-article.html', context)


@login_required(login_url='login')
def writeArticle(request):
    profile = request.user.profile
    form = ArticleForm()

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid:
            article = form.save(commit=False)
            article.owner = profile
            article.save()
            messages.success(request, 'Article was added successfully!')
            return redirect('account')

    context = {
        'title': 'Write Article - NOELIS Author Blog',
        'form': form
    }

    return render(request, 'articles/article-form.html', context)


@login_required(login_url='login')
def editArticle(request, pk):
    profile = request.user.profile
    article = profile.article_set.get(id=pk)
    form = ArticleForm(instance=article)

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid:
            form.save()
            return redirect('articles')

    context = {
        'title': 'Edit Article - NOELIS Author Blog',
        'form': form
    }

    return render(request, 'articles/article-form.html', context)


@login_required(login_url='login')
def deleteArticle(request, pk):
    profile = request.user.profile
    article = profile.article_set.get(id=pk)

    article.delete()
    messages.success(request, 'Project was deleted successfully!')
    return redirect('account')
