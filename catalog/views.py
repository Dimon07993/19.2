from django.shortcuts import render


#def index(request):
#   return render(request, 'catalog/index.html')

def home_view(request):
    """Контроллер для отображения домашней страницы."""
    return render(request, 'catalog/home.html')


def contact_view(request):
    """Контроллер для отображения страницы с контактной информацией."""
    return render(request, 'catalog/contact.html')
