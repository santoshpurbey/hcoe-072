from django.contrib import admin

from .models import Deposit, Withdraw
from .forms import DepositForm, WithdrawForm

@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    form = DepositForm


@admin.register(Withdraw)
class WithdrawAdmin(admin.ModelAdmin):
    form  = WithdrawForm
    autocomplete_fields = ['account_name']

    list_display = ('account_name', 'amount','pay_against','check_no', 'transaction_date')

# admin.site.register(Deposit)
# admin.site.register(Withdraw)
