# catalog/management/commands/populate_data.py
from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Populate the database with initial data'

    def handle(self, *args, **kwargs):
        # Очистка базы данных
        Category.objects.all().delete()
        Product.objects.all().delete()

        # Заполнение базы данных из фикстур
        call_command('loaddata', 'catalog/fixtures/catalog_data.json')

        self.stdout.write(self.style.SUCCESS('Database populated successfully'))
