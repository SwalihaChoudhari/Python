class order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    
    def showDetails(self):
        print(f"Item: {self.item}, Price: {self.price}")
    
    def __gt__(self,o2):
        return self.price>o2.price
            

o1=order("Chips",20)
o1.showDetails()
o2=order("tea",15)
o2.showDetails()
print(o1>o2)