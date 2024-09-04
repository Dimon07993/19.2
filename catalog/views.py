from django.shortcuts import render

def home_view(request):
    """Контроллер для отображения домашней страницы."""
    return render(request, 'catalog/home.html')

def contacts_view(request):
    """Контроллер для отображения страницы с контактной информацией."""
    return render(request, 'catalog/contacts.html')