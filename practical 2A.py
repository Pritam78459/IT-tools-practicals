class Bank:
    #creating a class bank.

    #accepting user details.
    user_name = str(input("Enter name:"))
    user_account_number = str(input("Enter account number:"))
    user_balance = 0
    
    def deposit(self,deposit_amount):
        #will deposit certain amount in the bank account.
        
        Bank.user_balance += deposit_amount
        print(f"Curernt balance is :{ Bank.user_balance}")
        
    def withdraw(self,withdraw_amount):
        #will withdraw certain amonunt from the bank account.
        
        Bank.user_balance -= withdraw_amount
        print(f"Curernt balance is :{ Bank.user_balance}")
        
    def user(self):
        #display user details.
        
        print(f"The name is { Bank.user_name}")
        print(f'The account number is { Bank.user_account_number}')
        print(f"Curernt balance is :{ Bank.user_balance}")
        

bank_object = Bank()        #creating an object for bank.

while True:
    
    print("1.User details.")
    print("2.Deposit amount.")
    print("3.Withdraw amount")
    print("4.Quit.")
    #creating an option system to navigate through the options.
    
    option = int(input("Enter option:"))
    if option == 2:
        bank_object.deposit(int(input("Enter deposit amount:")))
    elif option ==3:
        bank_object.withdraw(int(input("Enter withdraw amount:")))
    elif option == 1:
        bank_object.user()
    elif option == 4:
        break  
