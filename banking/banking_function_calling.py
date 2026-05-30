import banking_functions

name=input("Enter your name :")
acn=int(input("Enter your account number :"))
balance=int(input("What is your balance :"))

while True:
    print("                ")
    print("*"*50)
    print("Welcome to the bank")
    print("             ")
    print("what service you want to use :")
    print("1.Show your balance")
    print("2.I want to debit money")
    print("3.I want to withdraw money")
    print("4.Exit")
    print("                    ")

    choice=int(input("Enter the number according to your required service :"))
    print("         ")
    if choice==1:
        banking_functions.show_balance(balance)

    elif choice==2:
        amount=int(input("Enter the amount you want to debit"))
        banking_functions.debit(balance,amount)

    elif choice==3:
        amount=int(input("Enter the amount you want to withdraw"))
        banking_functions.withdraw(balance,amount)

    elif choice==4:
        print("Thank you for using our services")
        break

    else:
        print("Invalid number , please enter a correct number")
                         
