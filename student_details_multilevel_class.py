class Student:
     #this class will accept the details of the student.

     def _accept_details_of_the_student(self):
          #this method will accept the details of the student.
          
          self.division = input("Enter the division: ")
          self.roll_no = int(input('Enter your roll number: '))
          self.semester = input("Enter your current semester: ")


class Marks(Student):
     #this class will accept the marks of the student.

     def _accept_marks(self):
          #this method will accept the marks of the student.

          subjects = ['DM','WP','OOP','DBMS','PP']
          self.marks = []               #contains the marks.
          for subject in subjects:
               self.marks.append(int(input(f"Enter marks for {subject} out of 100: ")))

class Total_percentage(Marks):
     #this class will calculate the total marks of the student.

     def __display_total_marks_and_percentage(self):
          #this method will display the total marks and the percentage.
          
          print(f"The total marks obtained is {sum(self.marks)}.")
          print(f"The total percentage obtained is {sum(self.marks)/500 * 100}.")

student_details = Total_percentage()                        #object for calling all the methods.
student_details._accept_details_of_the_student()
student_details._accept_marks()
student_details._display_total_marks_and_percentage()     
    
