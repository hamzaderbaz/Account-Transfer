from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Account, Transaction
from .forms import TransferForm
from decimal import Decimal
import uuid

class AccountListViewTestCase(TestCase):
    def test_account_list_view(self):
        response = self.client.get(reverse('list_accounts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/list_accounts.html')

class AccountDetailViewTestCase(TestCase):
    def setUp(self):
        self.account = Account.objects.create(id=uuid.uuid4(), name='Test Account', balance=Decimal('100.00'))

    def test_account_detail_view(self):
        response = self.client.get(reverse('account_detail', kwargs={'pk': self.account.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/account_detail.html')
        self.assertContains(response, self.account.name)

class TransferFundsViewTestCase(TestCase):
    def setUp(self):
        self.account1 = Account.objects.create(id=uuid.uuid4(), name='Account 1', balance=Decimal('100.00'))
        self.account2 = Account.objects.create(id=uuid.uuid4(), name='Account 2', balance=Decimal('200.00'))

    def test_transfer_funds_view_get(self):
        response = self.client.get(reverse('transfer_funds'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/transfer_funds.html')
        self.assertIsInstance(response.context['form'], TransferForm)

    def test_transfer_funds_view_post_success(self):
        form_data = {
            'from_account': self.account1.id,
            'to_account': self.account2.id,
            'amount': '50.00'
        }
        response = self.client.post(reverse('transfer_funds'), form_data)
        self.assertRedirects(response, reverse('list_accounts'))
        self.account1.refresh_from_db()
        self.account2.refresh_from_db()
        self.assertEqual(self.account1.balance, Decimal('50.00'))
        self.assertEqual(self.account2.balance, Decimal('250.00'))

        self.assertEqual(Transaction.objects.count(), 1)
        transaction = Transaction.objects.first()
        self.assertEqual(transaction.from_account, self.account1)
        self.assertEqual(transaction.to_account, self.account2)
        self.assertEqual(transaction.amount, Decimal('50.00'))

    def test_transfer_funds_view_post_insufficient_funds(self):
        form_data = {
            'from_account': self.account1.id,
            'to_account': self.account2.id,
            'amount': '150.00'  
        }
        response = self.client.post(reverse('transfer_funds'), form_data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, b'Insufficient funds')
        self.account1.refresh_from_db()
        self.account2.refresh_from_db()
        self.assertEqual(self.account1.balance, Decimal('100.00'))
        self.assertEqual(self.account2.balance, Decimal('200.00'))

class AccountImportViewTestCase(TestCase):
    def test_import_accounts_view_get(self):
        response = self.client.get(reverse('import_accounts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/import_accounts.html')

    def test_import_accounts_view_post_success(self):
        csv_content = """ID,Name,Balance
e1b9f419-f587-47bd-ab4f-efd75b27e094,Account 1,100.00
e1b9f419-f587-47bd-ab4f-efd75b27e092,Account 2,200.00
e1b9f419-f587-47bd-ab4f-efd75b27e091,Account 3,300.00
"""
        csv_file = SimpleUploadedFile("accounts.csv", csv_content.encode(), content_type="text/csv")
        response = self.client.post(reverse('import_accounts'), {'file': csv_file})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Account.objects.count(), 3)
        self.assertEqual(Account.objects.get(name='Account 1').balance, Decimal('100.00'))
        self.assertEqual(Account.objects.get(name='Account 2').balance, Decimal('200.00'))
        self.assertEqual(Account.objects.get(name='Account 3').balance, Decimal('300.00'))

    def test_import_accounts_view_post_invalid_file(self):
        txt_content = "This is not a CSV file."
        txt_file = SimpleUploadedFile("accounts.txt", txt_content.encode(), content_type="text/plain")
        response = self.client.post(reverse('import_accounts'), {'file': txt_file})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, b'Invalid file format')
