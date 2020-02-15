import math    #importing math module.

class Shape:
     #the base class for all the classes.

     #initialising none values.
     _length = None
     _breadth = None
     _side = None
     _radius = None
     _x_axis_length = None
     _y_axis_length = None

     def __init__(self,length,breadth,
                  side,radius,x_axis_length
                  ,y_axis_length):

          #initializing protected shape values.
          self._length = length
          self._breadth = breadth
          self._side = side
          self._radius = radius
          self._x_axis_length = x_axis_length
          self._y_axis_length = y_axis_length

class Square(Shape):
     #calculating area for square.

     #initializing values for square
     def __init__(self,side):
          Shape.__init__(self,None,None,side,None,None,None)

     def calculate_area_of_square(self):
          #calculating area of square

          print(f"Area of the square is{self._side ** 2}")


class Rectangle(Shape):
     #calculating area for rectangle.

     #initializing values for rectangle.
     def __init__(self,length,breadth):
          Shape.__init__(self,length,breadth,None,None,None,None)

     def calculate_area_of_rectangle(self):
          #calculating area of rectangle

          print(f"Area of rectangle is {self._length * self._breadth}")


class Circle(Shape):
     #calculating area for circle.

     #initializing values for circle.
     def __init__(self,radius):
          Shape.__init__(self,None,None,None,radius,None,None)

     def calculate_area_of_circle(self):
          #calculating area of circle.

          print(f"Area of circle is {math.pi * self._radius ** 2}")


class Ellipse(Shape):
     #calculating area for ellipse.

     #initializing values for ellipse.
     def __init__(self,x_axis_length,y_axis_length):
          Shape.__init__(self,None,None,None,None,x_axis_length,y_axis_length)

     def calculate_area_of_ellipse(self):
          #calculating area of circle.

          print(f"Area of ellipse is {math.pi * self._x_axis_length * self._y_axis_length}")

#user options.
while True:
     print("1.Square.")
     print("2.Rectangle.")
     print("3.Circle.")
     print("4.Ellipse.")
     print("5.Quit.")
     
     user_option = int(input("Enter any of the option above:"))

     #calling user options
     if user_option == 1:
          Square_object = Square(int(input("Enter side: ")))                    #creating objects for square.
          Square_object.calculate_area_of_square()                              #calling calculation function.
     elif user_option == 2:
          Rectange_object = Rectangle(int(input("Enter length: ")),int(input("Enter breadth: ")))        #creating objects for rectangle.
          Rectange_object.calculate_area_of_rectangle()                                                                 #calling calculation function.
     elif user_option == 3:
          Circle_object = Circle(int(input("Enter radius: ")))                    #creating objects for circle.
          Circle_object.calculate_area_of_circle()                                 #calling calculation function.
     elif user_option == 4:
          Ellipse_object = Ellipse(int(input("Enter x axis length: ")),int(input(" Enter y axis length: ")))  #creating objects for ellipse.
          Ellipse_object.calculate_area_of_ellipse()                                                                              #calling calculation function.
     elif user_option == 5:
          break                                                       #getting out of loop.
     else:
          print("Enter correct option!")                    #if wrong options selected.
     
     



          
