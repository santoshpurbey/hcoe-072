class Error(Exception):
    pass


class InvalidAmount(Error):
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return 'Invalid Amount: {}'.format(self.amount)

    def __repr__(self):
        return 'Invalid Amount: {}'.format(self.amount)



class InsufficientBalance(Error):

    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount

    def __str__(self):
        return 'amount: {}, current balance: {}'.format(self.amount, self.balance)
