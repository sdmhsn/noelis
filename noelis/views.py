from django.shortcuts import render
from django.views.defaults import page_not_found


def index(request):
    context = {
        'title': 'Home - NOELIS Author Blog'
    }
    return render(request, 'index.html', context)


# def handle_not_found(request, exception):
#     return render(request, 'not-found.html', status=404)
#     # return page_not_found(request, exception, template_name="not-found.html")
    
def custom_404(request, exception):
    # return render(request, '404.html', status=404)
    return render(request, '404.html', status=404)