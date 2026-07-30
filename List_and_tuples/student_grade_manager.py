tup=("Maths", "Science", "English")
maths = int(input("Maths marks: "))
sci = int(input("Science marks: "))
eng = int(input("English marks: "))
marks=[]
marks.append(maths)
marks.append(sci) 
marks.append(eng) 
print("\nMarks: ",marks)
if 100 in marks:
    print("\nstudent have scored out of out in one subject ")
else:
    print("\nstudent did not score out of out in any subject")
marks.sort()
print("\nsorted marks: ",marks)
print("\nHighest marks: ",marks[2])
print("Lowest marks: ",marks[0])
