# from django.urls import path
# from .views import AccountListView, AccountDetailView, TransferFundsView, AccountImportView

# urlpatterns = [
#     path('accounts/', AccountListView.as_view(), name='list_accounts'),
#     # path('accounts/<uuid:pk>/', AccountDetailView.as_view(), name='account_detail'),
#     path('<int:pk>/', AccountDetailView.as_view(), name='account_detail'),
#     path('transfer/', TransferFundsView.as_view(), name='transfer_funds'),
#     path('import/', AccountImportView.as_view(), name='import_accounts'),
# ]


# accounts/urls.py

from django.urls import path
from .views import AccountListView, AccountDetailView, TransferFundsView, AccountImportView

urlpatterns = [
    path('accounts/', AccountListView.as_view(), name='list_accounts'),
    path('<uuid:pk>/', AccountDetailView.as_view(), name='account_detail'),
    path('transfer/', TransferFundsView.as_view(), name='transfer_funds'),
    path('import/', AccountImportView.as_view(), name='import_accounts'),
]
