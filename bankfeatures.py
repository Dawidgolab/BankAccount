class BankFeatures:
    def __init__(self, userCash):
        self.userCash = userCash
        self.account = userCash


    def deposit(self, amount):
        self.account += amount


    def withdrawal(self, amount):
        self.account -= amount


    def __str__(self):
        return (f"Your current account status: {self.account} zł\n"
                f"--------------------------------------------------")