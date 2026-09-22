class complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    def showNumber(self):
        print(f"{self.real} + {self.img}i")
    def __add__(self, num2):
        newreal=self.real + num2.real
        newimg=self.img + num2.img
        return complex(newreal, newimg)
    
num1=complex(3,4)
num1.showNumber()

num2=complex(4,5)
num2.showNumber()

num3=num1+num2
num3.showNumber()
