class employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary
    
    def showDetails(self):
        print(f"Role: {self.role}, Department: {self.dept}, Salary: {self.salary}")
       
class engineer(employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer", "IT" ,"75000")

engg1=engineer("Elon musk",40)
engg1.showDetails()