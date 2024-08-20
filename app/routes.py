from django.urls import path
from app.views import delete_transaction, edit_transaction, index, print_bill_page, transactions



urlpatterns = [
    path('', index, name="index-page"),
    path('transactions/', transactions, name="transactions-page"),
    path('transactions/edit/<int:meal_id>/', edit_transaction, name="edit-transaction"),
    path('transactions/delete/<int:meal_id>/', delete_transaction, name="delete-transaction"),
    path('transactions/print/<int:meal_id>/', print_bill_page, name="print-bill-page"),
]