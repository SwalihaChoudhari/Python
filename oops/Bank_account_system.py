class account:
    def __init__(self,acc_no,name,balance):
        self.acc_no=acc_no
        self.name=name
        self.__balance=balance
    
    @property
    def balance(self):
        return self.__balance
    
    
    def deposit(self,amount):
        self.__balance= self.__balance +amount
    
    def withdraw(self,amount):
        if amount<=self.__balance:
         self.__balance= self.__balance - amount
        else:
            print("Insuficiant balance")
    
    def checkBalance(self):
        print(f"Your balance is: {self.__balance}")
    
    def AccDetails(self):
        print("Account Number: ",self.acc_no)
        print("Account Name: ", self.name )
        print("Your Balance: ",self.__balance)
        

account1=account(12345,"Ravi Kishan",500000)
print("===== BANK ACCOUNT SYSTEM =====")
print("1. Deposit")
print("2. Withdraw")
print("3. Check Balance")
print("4. Account Details")
print("5. Exit")

while True:  
    choice = int(input("Enter your choice: "))
    if choice==1:
        amount=int(input("Enter amount u want to deposit:"))
        account1.deposit(amount)
        print("Your balance is:", account1.balance)
        
    elif choice==2:
        amount=int(input(("Enter amount u want to withdraw:  ")))
        account1.withdraw(amount)
        print("Your balance is:", account1.balance) 
        
    elif choice==3:
        print("Your balance is:", account1.balance)
       
    elif choice==4:
        account1.AccDetails()   
          
    elif choice==5:
        print("Exit")    
        break
    else:
        print("invalid choice try again!")



