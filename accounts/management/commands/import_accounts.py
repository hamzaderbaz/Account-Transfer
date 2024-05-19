import csv
from decimal import Decimal
from django.core.management.base import BaseCommand
from accounts.models import Account

class Command(BaseCommand):
    help = 'Import accounts from accounts.csv'

    def handle(self, *args, **kwargs):
        with open('accounts.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                account_id = row['ID']
                account_name = row['Name']
                balance = Decimal(row['Balance'])
                
                account, created = Account.objects.update_or_create(
                    id=account_id,
                    defaults={
                        'name': account_name,
                        'balance': balance
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Account {account_id} created'))
                else:
                    self.stdout.write(self.style.SUCCESS(f'Account {account_id} updated'))

        self.stdout.write(self.style.SUCCESS('Successfully imported accounts'))
