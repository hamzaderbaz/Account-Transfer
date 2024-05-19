from django import forms
from .models import Transaction

class TransferForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['from_account', 'to_account', 'amount']
