s1=int(input("Enter marks of subject1: "))
s2=int(input("Enter marks of subject2: "))
s3=int(input("Enter marks of subject3: "))
s4=int(input("Enter marks of subject4: "))
s5=int(input("Enter marks of subject5: "))

def calculate_total(s1,s2,s3,s4,s5):
    total=s1+s2+s3+s4+s5
    return total

def calculate_percentage(total):
    percentage=((total)/500)*100
    return percentage

def calculate_grade(percentage):
    if percentage>=90:
        return "A"
    elif percentage>=80:
        return "B"
    elif percentage>=70:
        return "C"
    elif percentage>=60:
        return "D"
    else:
        return "F"

def display_result(sum,percent,grade):
    print("=====RESULTS=========")
    print("Total marks: ",total)
    print("percentage obtained: ", percent)
    print("Grade obtained: ",grade)
    print("=====================")
    
total=calculate_total(s1,s2,s3,s4,s5)
percent=calculate_percentage(total)
grade=calculate_grade(percent)
display_result(total,percent,grade)