
    
balance=1000
def deposit(amount,balance):
    balance=balance+amount
    return balance
def withdraw(amount,balance):
    if amount > balance:
        print("Insufficient Balance!")
    balance=balance-amount
    return balance
def check_balance(balance):
    print("Current balance:",balance)
    

while True:
 print("\n _____Mini_banking_System_____")
 print("1.Deposit")
 print("2.Withdraw")
 print("3.Check your balance")
 print("4.Exit")
 choice=int(input("Enter your choice:"))

 if choice==1:
    amount=int(input("\nEnter amount to deposit: "))
    balance=deposit(amount,balance)
    print("Deposited successfully")
    print("\nAvailable balance: ",balance)
 elif choice==2:
    amount=int(input("\nEnter amount to withdraw: "))
    balance=withdraw(amount,balance)
    print("\nwithdraw successful")
    print("\nAvailable balance: ",balance)

 elif choice==3:
    check_balance(balance)
 elif choice==4:
    print("\nThank you for using our bank")
    break
 else:
      print("\nInvalid choice,Try again")
     
   
    