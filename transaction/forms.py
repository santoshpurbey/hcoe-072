from django import forms

from .models import Deposit, Withdraw
from customer.models import Profile


class DepositForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        initial_choice = self.fields['transaction_type'].widget.choices[1]
        self.fields['transaction_type'].initial = initial_choice
        self.fields['transaction_type'].widget.attrs['disabled'] = True

    class Meta:
        model = Deposit
        fields = ('transaction_type','account_name', 'amount', 'vouch_no','deposite_by',\
         'contact_no','source_of_funds','method')

    def save(self, commit=True, *args, **kwargs):
        obj = super().save(commit=False,*args, **kwargs)
        profile = Profile.objects.get(pk=obj.account_name.id)
        amount = self.cleaned_data['amount']
        if obj.id:
            old_amount = Deposit.objects.get(pk= obj.id).amount
            profile.withdraw(old_amount)

        profile.deposite(amount)
        profile.save()
        return obj



class WithdrawForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        initial_choice = self.fields['transaction_type'].widget.choices[2]
        self.fields['transaction_type'].initial = initial_choice
        self.fields['transaction_type'].widget.attrs['disabled'] = True

    class Meta:
        model = Withdraw
        fields = ('transaction_type','account_name', 'amount', 'check_no','pay_against',)

    def save(self, commit=True, *args, **kwargs):
        obj = super().save(commit=False,*args, **kwargs)
        profile = Profile.objects.get(pk=obj.account_name.id)
        amount = self.cleaned_data['amount']
        if obj.id:
            old_amount = Withdraw.objects.get(pk= obj.id).amount
            profile.deposite(old_amount)

        profile.withdraw(amount)
        profile.save()
        return obj
