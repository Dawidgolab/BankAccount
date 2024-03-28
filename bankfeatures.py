from result import Ok,Error
class BankFeatures:
    def __init__(self, userCash):
        self.userCash = userCash
        self.account = userCash


    def deposit(self, amount):
        self.account += amount


    def try_withdrawal(self, amount):
        if self.account == 0 or amount > self.account:
            return Error("You dont have enough money to do this operation\n")
        else:
            self.account -= amount
            return Ok( f"You withdrew from the bank: {amount} zł\n")


    def __str__(self):
        return (f"-> Current account status: {self.account} zł\n")