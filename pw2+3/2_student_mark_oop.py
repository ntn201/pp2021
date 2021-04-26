from datetime import date
import numpy as np

class Class:
    def __init__(self):
        self.__students = []
        self.__courses = []
    
    def enroll_student(self,id,name,dob):
        student = Student(id,name,dob)
        if student.is_valid():
            self.__students.append(student)
            self.__students = sorted(self.__students, key=lambda s: s.get_id())
            return True
        return False
    
    def add_course(self,id,name,credits):
        course = Course(id,name,credits)
        if (course.is_valid()):
            self.__courses.append(course)
            self.__courses = sorted(self.__courses, key=lambda c: c.get_id())
            return True
        return False
    
    def unenroll_student(self,id):
        for i in range(len(self.__students)):
            if self.__students[i].get_id() == id:
                self.__students.pop(i)
                return True
        return False

    def remove_course(self,id):
            for i in range(len(self.__course)):
                if self.__courses[i].get_id() == id:
                    self.__courses.pop(i)
                    return True
            return False

    def get_student(self, id):
        for i in range(len(self.__students)):
            if self.__students[i].get_id() == id:
                return self.__students[i]
        return None
    
    def get_course(self, id):
        for i in range(len(self.__courses)):
            if self.__courses[i].get_id() == id:
                return self.__courses[i]
        return None

    def list_students(self):
        print("There are {no_students} students!".format(no_students=len(self.__students)))
        for s in self.__students:
            print("{id}: {name}".format(id=s.get_id(), name=s.get_name()))
        print()

    def list_courses(self):
            print("There are {no_courses} courses!".format(no_courses=len(self.__courses)))
            for c in self.__courses:
                print("{id}: {name}".format(id=c.get_id(), name=c.get_name()))
            print()


class Course:
    def __init__(self,id,name,credits):
        if self.validate_id(id):
            self.__id = id
        if self.validate_name(name):
            self.__name = name
        if self.validate_credits(credits):
            self.__credits = credits
        self.__marks = {}

    def __str__():
        return self.__name

    def validate_id(self,id):
        return type(id) == int and id > 0

    def validate_name(self,name):
        return type(name) == str and len(name) > 0

    def validate_credits(self,credits):
        return type(credits) == int and credits > 0

    def validate_mark(self,mark):
        return type(mark) == float and 0.0 <= mark <= 20.0

    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_student_mark(self,id):
        return self.__marks.get(str(id))
    
    def set_name(self,name):
        if self.validate_name(name):
            self.__name = name
            return True
        return False

    def set_student_mark(self,id,mark):
        if self.validate_mark(mark):
            self.__marks[str(id)] = mark
            return True
        return False

    def get_average_mark(self):
        return np.array(self.__marks.values()).mean()

    def is_valid(self):
        return self.validate_id(self.__id) and self.validate_name(self.__name) and self.validate_credits(self.__credits)


class Student:
    enrolled_id = {}
    enrolled_id.setdefault(False)

    def is_enrolled(self,id):
        return self.enrolled_id.get(str(id),False)

    def enroll_course(self,course):
        self.__enrolled_courses[str(course.get_id())] = course

    def __init__(self,id,name,dob):
        if self.validate_id(id):
            self.__id = id
            self.enrolled_id[str(id)] = True
        if self.validate_name(name):
            self.__name = name
        self.__dob = self.format_dob(dob)
        self.__enrolled_courses = {}
    
    def __str__(self):
        return self.__name

    def validate_id(self,id):
        return type(id) == int and id > 0 and (not self.is_enrolled(id))
    
    def validate_name(self,name):
        return type(name) == str and len(name) > 0
    
    def format_dob(self,dob):
        day, month, year = map(int,dob.split("-"))
        try:
            return date(year,month,day)
        except:
            return None

    def set_id(self,id):
        if validate_id(id):
            self.enrolled_id[str] = False
            self.__id = id
            self.enrolled_id[str(id)] = True
            return True
        return False
    
    def set_name(self,name):
        if validate_name(name):
            self.__name = name
            return True
        return False

    def set_dob(dob):
        self.__dob = self.format_dob(dob)
        return True

    def set_mark(self,course_id,mark):
        return self.__enrolled_courses.get(str(course_id)).set_student_mark(self.__id,mark)

    def get_id (self):
        return self.__id
    
    def get_name(self):
        return self.__name

    def get_dob(self):
        return "{D}-{M}-{Y}".format(D=self.__dob.day,M=self.__dob.month,Y=self.__dob.year)

    def get_mark(self,course_id):
        return self.__enrolled_courses.get(str(id)).get_student_mark(self.__id)
    
    def is_valid(self):
        return self.validate_id(self.__id) and self.validate_name(self.__name) and (self.__dob != None)

    
class Program():
    def __init__(self):
        self.__class = Class()

    def input_student(self):
        id = int(input("Enter student id: "))
        name = input("Enter student name: ")
        dob = input("Enter student's date of birth (DD-MM-YYYY): ")
        if self.__class.enroll_student(id,name,dob):
            print("Student enrolled\n")
        else:
            print("Some errors happened\n")

    def input_course(self):
        id = int(input("Enter course id: "))
        name = input("Enter course name: ")
        credits = int(input("Enter course credits: "))
        if self.__class.add_course(id,name,credits):
            print("Course added\n")
        else:
            print("Some errors happened\n")

    def input_mark(self):
        student_id = int(input("Enter student id: "))
        course_id = int(input("Enter course id: "))
        mark = float(input("Enter mark: "))
        course = self.__class.get_course(course_id)
        student = self.__class.get_student(student_id)
        student.enroll_course(course)
        if course.set_student_mark(student_id,mark):
            print("Mark saved\n")
        else:
            print("Some errors happened\n")

    def list_student(self):
        self.__class.list_students()

    def list_course(self):
        self.__class.list_courses()

    def get_student_mark(self):
        student_id = int(input("Enter student id: "))
        course_id = int(input("Enter course id: "))

        student = self.__class.get_student(student_id)
        course = self.__class.get_course(course_id)
        if student == None:
            print("Student have not enrolled yet\n")
            return None
        if course == None:
            print("The course does not exists\n")

        mark = course.get_student_mark(student_id)
        if mark != None:
            print("Student id: {id} - {name}: {mark}\n".format(id=student_id, name=course.get_name(), mark=mark))
        else:
            print("Not updated\n")
    

    def option_prompt(self):
        print("""Select one of the below options:
        1. List courses.
        2. List students.
        3. Input a student.
        4. Input a course.
        5. Input student mark.
        6. Get student mark.
        7. Exit.""")
        option = int(input())
        return option
        
    def main(self):
        print("Student management program")
        while True:
            option = self.option_prompt()
            if option == 1:
                self.list_course()
            elif option == 2:
                self.list_student()
            elif option == 3:
                self.input_student()
            elif option == 4:
                self.input_course()
            elif option == 5:
                self.input_mark()
            elif option == 6:
                self.get_student_mark()
            elif option == 7:
                break
            else:
                print("Invalid option!")
    


program = Program()
program.main()