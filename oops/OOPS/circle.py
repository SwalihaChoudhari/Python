class circle:
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        area= (3.14 * self.radius * self.radius)
        return area
        
    def perimeter(self):
        perimeter=(2* 3.14 * self.radius)
        return perimeter 
    
rad1=circle(21)
print(rad1.area())
print(rad1.perimeter())