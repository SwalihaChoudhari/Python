while True:
 print("===== NOTE MANAGER =====") 
 print("1. Add Note")
 print("2. View Notes")
 print("3. Search Notes")
 print("4. Exit")
 choice=int(input("Enter your choice: "))
 if choice==1:
     with open("notes.txt","a") as f:
         note=input("Enter your note:")
         data=f"{note}/n"
         f.write(data)
 elif choice==2:
     with open("notes.txt","r") as f:
         data=f.read()
         print(data)
 elif choice==3:
     with open("notes.txt","r") as f:
         data=f.read()
         word=input("Search for your notes: ")
         if word in data:
             print("found")
         else:
             print("Not found")
 elif choice==4:
     print("Thnakyou for using notes manager")
     break
 else:
     print("invalid entry, Try again!")