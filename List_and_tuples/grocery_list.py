grocery=[]
item1=input("Enter first item: ")
item2=input("Enter second item: ")
item3=input("Enter third item: ")
item4=input("Enter forth item: ")
grocery.append(item1)
grocery.append(item2)
grocery.append(item3)
grocery.append(item4)
print("Your grocery list is:",grocery)

del_item=(input("which item u want to delete? " ))
if del_item in grocery:
    grocery.remove(del_item)
    print(f"Item {del_item} deleted")
else:
    print("Item not found!")
print("Final list: ",grocery)
print(len(grocery))
