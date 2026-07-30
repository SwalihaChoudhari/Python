password=input("Enter your password: ")
if(len(password)<6):
    print("WEAK PASSWORD!")
    print("Add more charactors.")
elif(6<=len(password)<=10):
    print("MEDIUM PASSWORD!")
else:
    print("STRONG PASSWORD!")
