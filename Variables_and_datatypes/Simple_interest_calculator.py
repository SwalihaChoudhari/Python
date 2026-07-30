Principal=int(input("Enter Original amount of money: "))
Rate=float(input("Enter the rate: "))
Time=int(input("Enter number of years: "))
SI = (Principal * Rate * Time) / 100
print("Simple interest is: ",round(SI,2))
