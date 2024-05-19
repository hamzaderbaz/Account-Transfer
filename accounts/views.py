from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, FormView, View
from django.views import View
from django.urls import reverse_lazy
from django.http import HttpResponseBadRequest, HttpResponse
from .models import Account, Transaction
from .forms import TransferForm
import csv
from decimal import Decimal

class AccountListView(ListView):
    model = Account
    template_name = 'accounts/list_accounts.html'
    context_object_name = 'accounts'

class AccountDetailView(DetailView):
    model = Account
    template_name = 'accounts/account_detail.html'
    context_object_name = 'account'

class TransferFundsView(FormView):
    template_name = 'accounts/transfer_funds.html'
    form_class = TransferForm
    success_url = reverse_lazy('list_accounts')

    def form_valid(self, form):
        from_account = form.cleaned_data['from_account']
        to_account = form.cleaned_data['to_account']
        amount = form.cleaned_data['amount']

        if from_account.balance < amount:
            return HttpResponseBadRequest("Insufficient funds")

        from_account.balance -= amount
        to_account.balance += amount
        from_account.save()
        to_account.save()

        Transaction.objects.create(
            from_account=from_account,
            to_account=to_account,
            amount=amount
        )

        return super().form_valid(form)

class AccountImportView(View):
    def get(self, request):
        return render(request, 'accounts/import_accounts.html')

    def post(self, request):
        if 'file' not in request.FILES:
            return HttpResponseBadRequest('No file uploaded')
        
        file = request.FILES['file']
        if not file.name.endswith('.csv'):
            return HttpResponseBadRequest('Invalid file format')

        try:
            reader = csv.DictReader(file.read().decode('utf-8').splitlines())
            for row in reader:
                account_id = row['ID']
                account_name = row['Name']
                balance = Decimal(row['Balance'])

                Account.objects.update_or_create(
                    id=account_id,
                    defaults={'name': account_name, 'balance': balance}
                )
            return HttpResponse('Accounts imported successfully', status=200)
        except Exception as e:
            return HttpResponseBadRequest(f'Error processing file: {str(e)}')