while True:
 print("===== EXPENSE TRACKER =====")
 print("1. Add Expense")
 print("2. View Expenses")
 print("3. Calculate Total")
 print("4. Search Expense")
 print("5. Exit")
 choice=int(input("Enter your choice: "))
 if choice==1:
  with open("expense.txt","a") as f:
     ctg=(input("Enter your category:"))
     ex=int(input("Enter your expense:"))
     data=f"{ctg},{ex}\n"
     f.write(data)
 elif choice==2:
  with open("expense.txt","r") as f:
      data=f.read()
      print(data)
 elif choice==3:
  with open("expense.txt","r") as f:
    data = f.readlines()
    total=0
    for line in data:
        amount=line.split(",")
        total+=int(amount[1])
    print("Total Expenses:", total)
 elif choice==4:   
     with open("expense.txt","r") as f:
         data=f.read()
         word=(input("Enter expense for search: "))
         if(word in data):
          print("found")      
         else:
          print("not found")
 elif choice==5:
     print("Thankyou for using our expense tracker ")
     break
 else:
     print("Invalid option, try agian ")
                                    