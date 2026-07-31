
while True:
 print("\n==== calculator ====")
 print("1.find factorial")
 print("2.Find  sum of first n natural numbers")
 print("3.Exit")

 choice=int(input("Enter ur choice:"))
 if choice==1:
    i=1
    fact=1
    n=int(input("Enter your number:"))
    while i<=n:
      fact*=i
      i+=1
    print(f"Factorial ={fact}")
 elif choice==2:
    total=0
    n=int(input("Enter your number:"))
    for i in range(1,n+1):
     total+=i
    print(f"sum={total}")
 elif choice==3:
    print("Thank you for using the calculator!")
    break
 else:
    print("Invalid choice ,Try again")