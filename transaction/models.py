from django.db import models

from customer.models import Profile

class BaseTransaction(models.Model):
    DEPOSIT = '0'
    WITHDRAW = '1'
    TRANSACTION_TYPE_CHOICES =(
        (DEPOSIT, 'Deposit'),
        (WITHDRAW, 'Withdraw'),
    )
    account_name = models.ForeignKey(Profile, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    transaction_type = models.CharField(max_length=1, choices=TRANSACTION_TYPE_CHOICES, blank=True)
    transaction_date = models.DateTimeField(auto_now_add=True)
    branch = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        abstract = True


class Deposit(BaseTransaction):
    CASH = '0'
    CHEQUE = '1'
    METHOD_CHOICES = (
        (CASH, 'Cash'),
        (CHEQUE, 'Cheque'),
    )

    vouch_no = models.PositiveIntegerField()
    deposite_by = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=20)
    source_of_funds = models.CharField(max_length=200, null=True, blank=True)
    method = models.CharField(choices=METHOD_CHOICES, max_length=200, default=CASH)

    def save(self, *args, **kwargs):
        self.transaction_type = self.DEPOSIT
        super().save(*args, **kwargs)

    def __str__(self):
        return 'Account {} amount {}'.format(self.account_name, self.amount)



class Withdraw(BaseTransaction):
    check_no = models.PositiveIntegerField()
    pay_against = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        self.transaction_type = self.WITHDRAW
        super().save(*args, **kwargs)
