import math

class Circle():

    ''' Clsss is used for finding the area and perimeter of the circle'''

    def __init__(self, radius):
        
        self.radius = radius
        self.pi = round(math.pi, 2)


    def area(self):
        ''' Function will return the area of circle'''
        return self.pi*self.radius**2

    def perimeter(self):
        ''' Function will return the perimeter of circle'''
        return 2*self.pi*self.radius

    

if __name__ == "main":
    C1 = Circle(109.8)
    print(C1.area())
    print(C1.perimeter())
