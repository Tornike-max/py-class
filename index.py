class Student():
    university = str('')  # This class attribute is not used in the class.

    def __init__(self, name, grade, age):
        self.name = name  # Initialize instance variables
        self.grade = grade
        self.age = age

    def __str__(self):
        return f"Name: [{self.name}], Age: [{self.age}] Grade: [{self.grade}]"

    def is_passing(self):
        if self.grade > 60:
            print(True)
        else:
            print(False)

    def increase_grade(self, inc):
        if inc < 5:
            print('There is no increment')
        self.grade += inc 
        print(f"Grade increased by {inc} points. total grade: {self.grade}")

def main():
    student = Student('tornike', 10, 22)
    student.increase_grade(61)
    student.is_passing()
    print(student)
    
main()