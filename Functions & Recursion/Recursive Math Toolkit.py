
def fact(n):
    if n==0 or n==1:
        return 1
    else:
       return fact(n-1)*n

    
def cal_sum(n):
    if n==0:
        return 0
    return cal_sum(n-1)+n
    

while True:
    print("\n===== Recursive Toolkit =====")
    print("1.find factorial")
    print("2.find Sum of N natural numbers")
    print("3.Exit")
    choice=int(input("Enter your choice:"))
    if choice ==1:
        num=int(input("Enter number: "))
        fact=fact(num)
        print(fact)
    elif choice==2:
        num=int(input("Enter number: "))
        total=cal_sum(num)
        print(total)
    elif choice==3:
        print("Thank you for using our toolkit")
        break
    else:
        print("Invalid choice! Please try again.")