from django.shortcuts import render


def index(request):
    context = {
        'title': 'Home - NOELIS Author Blog'
    }
    return render(request, 'index.html', context)
