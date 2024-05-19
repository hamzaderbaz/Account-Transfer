from django.contrib import admin
from .models import Account, Transaction

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'balance')
    search_fields = ('name',)
    list_filter = ('balance',)
    ordering = ('name',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'from_account', 'to_account', 'amount', 'timestamp')
    list_filter = ('timestamp',)
    ordering = ('-timestamp',)
