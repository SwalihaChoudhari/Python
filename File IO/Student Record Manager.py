while True:
 print("==== STUDENT RECORD MANAGER =====")
 print("1. Add Student")
 print("2. View Students")
 print("3. Search Student")
 print("4. Delete Student")
 print("5. Exit")
 choice=int(input("Enter your choice: "))
 if choice==1:
    with open("student.txt","a") as f:
         id=int(input("Enter student id: "))
         name=(input("Enter student name: "))
         marks=int(input("Enter student marks: "))
         data=f"{id},{name},{marks}\n"
         f.write(data)
 elif choice==2: 
    with open("student.txt","r") as f: 
         data=f.read() 
         print(data)
 elif choice==3:
    with open("student.txt","r") as f:
        data=f.read()
        word=(input("Enter student info for search: "))
        if(word in data):
            print("found")      
        else:
            print("not found")  
 elif choice==4:
   with open("student.txt", "r") as f:
        data = f.readlines()

        del_id = int(input("Enter student id to delete: "))

        new_data = []

        for line in data:
         student = line.split(",")

        if int(student[0]) != del_id:
            new_data.append(line)

        with open("student.txt", "w") as f:
         f.writelines(new_data)

        print("Student deleted successfully!")
        
 elif choice==5:
        print("Exiting the program...")
        break
 else:
        print("Invalid choice. Please try again.")

