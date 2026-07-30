contacts={
    "Ravi": 3728178372,
    "Priya": 7564893209,
    "Rahul": 6358216789,
    "Varsha": 7469023465,
    "Sameer": 4537829012
}
name=input("Enter name: ")
if name in contacts:
    print("number: ",contacts.get(name))
else:
    print("Contact not found")
