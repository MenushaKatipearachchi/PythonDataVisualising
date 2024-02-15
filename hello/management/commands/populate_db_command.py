from django.core.management.base import BaseCommand
from hello.populate_db import populate_db

class Command(BaseCommand):
    help = 'Populates the database'

    def handle(self, *args, **options):
        populate_db()
