class Student:
    'A student class'

    # initialization or constructor method of
    def __init__(self):  
        # class Student
        self.name = input('enter student name:')
        self.rollno = input('enter student rollno:')
  
    # displayStudent method of class Student
    def displayStudent(self):  
        print("Name:", self.name, "Rollno:", self.rollno)
  
  
stu1 = Student()
stu2 = Student()
stu3 = Student()
stu1.displayStudent()
stu2.displayStudent()
stu3.displayStudent()
print('total no. of students:', Student.stuCount)