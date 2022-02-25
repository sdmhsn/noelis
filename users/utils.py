from .models import Profile
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginateAuthors(request, authors, results):
    page = request.GET.get('page')
    paginator = Paginator(authors, results)

    try:
        authors = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        authors = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        authors = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, authors


def searchAuthors(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    authors = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) |
        # Q(short_intro__icontains=search_query) |
        Q(location__icontains=search_query)
    )

    return authors, search_query
