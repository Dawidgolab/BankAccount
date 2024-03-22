class BankFeatures:
    def __init__(self, userCash):
        self.userCash = userCash
        self.account = userCash


    def deposit(self, amount):
        self.account += amount


    def withdrawal(self, amount):
        if self.userCash == 0 or amount > self.userCash:
            print("You dont have enough money to make this operation!!!")
            print(self.__str__())
        else:
            self.account -= amount
            print(self.__str__())


    def __str__(self):
        return (f"Your current account status: {self.account} zł\n"
                f"--------------------------------------------------")