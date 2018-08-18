from django.db import models

from .errors import InvalidAmount

class Profile(models.Model):
    """
    Customer Profile
    """

    ACCOUNT_NO = 1000000
    CURRENT = '0'
    SAVING = '1'

    ACCOUNT_TYPE_CHOICES = (
    (CURRENT, 'Current'),
    (SAVING, 'Saving'),
    )

    name = models.CharField(max_length=30)
    address = models.CharField(max_length=40)
    dob = models.DateField()
    citizenship_no = models.CharField(max_length=15)
    contact_no = models.CharField(max_length=10)
    account_no = models.PositiveIntegerField(unique=True, blank=True)
    account_type = models.CharField(max_length=1, choices=ACCOUNT_TYPE_CHOICES, default=SAVING)
    balance = models.DecimalField(decimal_places=2, max_digits=12,default=0.0)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_balance(self):
        return self.balance

    def save(self, *args, **kwargs):
        if self.id is None:
            self.account_no = Profile.ACCOUNT_NO
            Profile.ACCOUNT_NO +=1
        super().save(*args, **kwargs)

    def deposite(self, amount):
        if amount < 0:
            raise InvalidAmount(amount)
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount < 0:
            raise InvalidAmount(amount)
        if self.balance < amount:
            raise InsufficientBalance(self.balance, amount)
        self.balance -= amount
        return self

    def __str__(self):
        return 'Name : {} Account No: {}'.format(self.name, self.account_no)
