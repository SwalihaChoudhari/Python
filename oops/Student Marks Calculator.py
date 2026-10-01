class student:
    def __init__(self,name,maths,science,computer):
        self.name=name
        self.maths=maths
        self.science=science
        self.computer=computer
    
    def __add__(self,std2):
        total=self.maths+std2.maths+self.science+std2.science+self.computer+std2.computer
        average=total/2
        return average
    
    def display_role(self):
     print("I am a student")
    
class teacher:
    def __init__(self,name,subject):
        self.name=name
        self.subject=subject
    
    def display_role(self):
        print("i am a teacher")   
        
std1=student("Tony",99,97,100)
std2=student("peter",97,96,98)
teacher1=teacher("Mrs. Smith", "Mathematics")
teacher1.display_role()
std1.display_role()
result=std1+std2
print(result)
