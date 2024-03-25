from bankfeatures import BankFeatures
class Bank:

    user = BankFeatures(userCash = int(input("Enter Your initial balance: ")))


    while True:
        choice = input("Select the option: 1.Show account status | 2.Deposit | 3.Withdrawal | 4.Exit: \n")
        if choice == '1':
            print(user)

        elif choice == '2':
            amountOfMoney = int(input("How much you want to deposit: "))
            user.deposit(amountOfMoney)
            print(user)

        elif choice == '3':
            amountOfMoney = int(input("How much you want to withdraw: "))
            result = user.try_withdrawal(amountOfMoney)
            print(result["message"], user)

        elif choice == '4':
            print("Good Bye!!")
            break
        else:
            print("You selected wrong option, try again!!!")


