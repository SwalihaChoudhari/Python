
print("\n=====Number Toolkit======")
print("1.odd or even")
print("2.prime or not")
print("3.factorial")
choice=int(input("Enter your choice:"))
if choice==1:
 def odd_or_even(n):
    if n%2==0:
        return "Even"
    else:
        return "Odd"
 result=odd_or_even(int(input("Enter number:")))
 print(result)

elif choice==2:
 def prime(n):
    if n<=1:
        return "not prime"
    for i in range(2,n):
     if n%i==0:
        return "not prime"
    return "prime"
 result2=prime(int(input("Enter number:")))
 print(result2)
elif choice==3:
 def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
 result3=factorial(int(input("Enter number:")))
 print(result3)
else:
    print("invalid entry,try again" )    
