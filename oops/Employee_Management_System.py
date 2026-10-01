class employee:
    def __init__(self,name,emp_id,salary):
        self.name=name
        self.emp_id=emp_id
        self.salary=salary
        
    def display_details(self):
        print("Employee ID: ",self.emp_id)
        print("Employee name: ",self.name)
        print("Employee salary: ",self.salary)
class engineer(employee):
    def __init__(self,name, emp_id, salary,prog_lang):
        super().__init__(name,emp_id,salary)
        self.prog_lang=prog_lang
    def display_engineer(self):
        super().display_details()
        print("programming language: ",self.prog_lang)
    
emp1=employee("swaliha",49,40000)
emp1.display_details()
print("\n")
eng1=engineer("Tony stark",7,3000,"python")
eng1.display_engineer()