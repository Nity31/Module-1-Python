def show_balance(balance):
    print("Your Current Balance is :",balance)


def debit(balance,amount):
    balance=amount+balance
    print("Your balance after debit money is :",balance)
    return balance

def withdraw(balance,amount):
    if balance>amount:
        balance=balance-amount
    print("Your balance after withdrawl is :",balance)
    return balance
        
