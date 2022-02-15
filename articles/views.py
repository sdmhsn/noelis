from django.shortcuts import render


def articles(request):
    context = {
        'title': 'Articles - NOELIS Author Blog',
    }
    return render(request, 'articles/articles.html', context)
