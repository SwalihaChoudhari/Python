while True:
    n=int(input("Enter a number: "))
    l=int(input("Enter limit:"))
    for i in range (1,l):
      mul=n*i
      print(f"{n}*{i}={mul}")
    choice=input("\nDo you want another table?(y/n):\n ")
    if choice=="n":
        print("Thank you")
        break



    