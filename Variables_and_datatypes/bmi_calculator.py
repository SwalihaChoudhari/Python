weight=float(input("Enter your wieght in kg:"))
height=float(input("Enter your height in m:"))
bmi=weight/(height*height)
print("Enter your BMI:",round(bmi,2))
if bmi < 18.5:
    print("Underweight")
elif bmi < 24.9:
    print("Normal weight")
elif bmi < 29.9:
    print("Overweight")
else:
    print("Obese")
