from django.core.management.base import BaseCommand
from django.db.migrations.recorder import MigrationRecorder

class Command(BaseCommand):
    help = 'Delete migration records for customer_management app in both default and session databases'

    def handle(self, *args, **kwargs):
        for db in ['default', 'session']:
            MigrationRecorder(connection=db).Migration.objects.filter(app='customer_management').delete()
            self.stdout.write(self.style.SUCCESS(f'Successfully deleted migration records for customer_management app in {db} database'))

