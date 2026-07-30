x=int(input("Enter your math marks: "))
y=int(input("Enter your Mongodb marks: "))
z=int(input("Enter your Dbms marks: "))
a=int(input("Enter your AI marks: "))
b=int(input("Enter your Bio marks: "))
c=int(input("Enter your Ada marks: "))

subjects={ "Maths": x,
    "Mongodb": y,
    "Dbms": z,
    "AI" : a,
    "Bio": b,
    "Ada": c
    }

total=(x+y+z+a+b+c)

percentage=(total/600)*100

if (percentage>=90):
    print("Grade A")
elif(percentage>=80):
    print("Grade B")
elif(percentage>=70):
    print("Grade C")
elif(percentage>=60):
    print("Grade D")
else:
    print("Fail")

print(subjects)
print(total)
print(percentage)