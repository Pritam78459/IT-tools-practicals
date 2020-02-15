#Abstract class code.

#importing reqiured modules.
from abc import ABC
import math

class Shape(ABC):
     #Abstract class

     #empty functions.
     def calculateArea(self):
          pass

     def calculatePerimeter(self):
          pass

     def noofsides(self):
          pass

class Square(Shape):
     #will display details about square.

     _side = int(input("Enter the length of side: "))       #Data for Square.

     def calculateArea(self):
          #Will calculate Area.
          
          print(f"The area of the square is {Square._side ** 2}.")

     def calculatePerimeter(self):
          #will calculate perimeter.
          
          print(f"The perimeter of the square if {4 * Square._side}.")

     def noofsides(self):
          #will tell number of sides
          
          print(f"The number of sides is 4.")

#the rest classes and methods are created in the same type.

class Rectangle(Shape):

     _length = int(input("Enter the length: "))
     _breadth = int(input("Enter the breadth: "))

     def calculateArea(self):
          print(f"The area of the square is {Rectangle._length * Rectangle._breadth}.")

     def calculatePerimeter(self):
          print(f"The perimeter of the square if {2 * (Rectangle._length + Rectangle._breadth)}.")

     def noofsides(self):
          print(f"The number of sides is 4.")

class Circle(Shape):

     _radius = int(input("Enter the radius: "))

     def calculateArea(self):
          print(f"The area of the square is {math.pi * Circle._radius ** 2}.")

     def calculatePerimeter(self):
          print(f"The perimeter of the square if {2 * math.pi * Circle._radius}.")

     def noofsides(self):
          print(f"It's a circle so there are infinite sides.")

class Ellipse(Shape):

     _x_axis_length = int(input("Enter x-axis length: "))
     _y_axis_length = int(input("Enter y-axis length: "))

     def calculateArea(self):
          print(f"Area of ellipse is {math.pi * Ellipse._x_axis_length * Ellipse._y_axis_length}")
          
     def calculatePerimeter(self):
          print(f"The perimeter of the square if {2  * math.pi * math.sqrt(((Ellipse._x_axis_length**2) + (Ellipse._y_axis_length ** 2))/2)}.")

     def noofsides(self):
          print(f"It's an ellipse so there are infinite sides.")

#Object creation and methods calling
#each class has a seperate object
#methods are called for each class

Square_object = Square()
Square_object.calculateArea()
Square_object.calculatePerimeter()
Square_object.noofsides()

Rectangle_object = Rectangle()
Rectangle_object.calculateArea()
Rectangle_object.calculatePerimeter()      
Rectangle_object.noofsides()

Circle_object  = Circle()
Circle_object.calculateArea()
Circle_object.calculatePerimeter() 
Circle_object.noofsides()

Ellipse_object = Ellipse()
Ellipse_object.calculateArea()
Ellipse_object.calculatePerimeter() 
Ellipse_object.noofsides()

      
