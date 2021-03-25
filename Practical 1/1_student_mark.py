from datetime import date

def input_no_student(course):
    no_students = int(input("Enter number of students: "))
    if no_studensts > 0:
        course["no_students"] = no_studensts
    else:
        print("Invalid number of students!")

def input_student(course):
    student_id = int(input("Enter student id: "))
    if student_id < 0:
        print("Invalid student id!")
        return None
    student_name = input("Enter student name: ")
    day, month, year = map(int,input("Enter student date of birth (DD-MM-YYYY): ").split("-"))
    student_dob = date(year,month,day)
    course["students"].append({
        "id": student_id,
        "name": student_name,
        "dob": student_dob,
        "marks": {}
    })
    course["students"] = sorted(course["students"], key = lambda s: s["id"])
    course["no_students"] += 1

def input_no_course(course):
    no_courses = int(input("Enter number of courses: "))
    if no_courses > 0:
        course["no_courses"] = no_courses
    else:
        print("Invalid number of courses!")

def input_course(course):
    course_id = int(input("Enter course id: "))
    if course_id < 0:
        print("Invalid course id!")
        return None
    course_name = input("Enter course name: ")
    course["courses"].append({
        "id": course_id,
        "name": course_name,
    })
    course["courses"] = sorted(course["courses"], key = lambda c: c["id"])
    course["no_courses"] += 1

def input_mark(course):
    student_id = int(input("Enter student id: "))
    course_id = int(input("Enter course id: "))
    mark = int(input("Enter mark: "))
    student_index = 0
    for i, stud in enumerate(course["students"]):
        if stud["id"] == student_id:
            student_index = i
            print(i)
            break
    course_name = ""
    for c in course["courses"]:
        if c["id"] == course_id:
            course_name = c["name"]
            break
    if course_name == "":
        print("Unknown course!")
        print()
        return None
    course["students"][student_index]["marks"][course_name] = mark

def list_student(course):
    print("There are {no_students} students!".format(no_students=course["no_students"]))
    for stud in course["students"]:
        print("{id}: {name}".format(id=stud["id"], name=stud["name"]))
    print()

def list_course(course):
    print("There are {no_courses} courses!".format(no_courses=course["no_courses"]))
    for course in course["courses"]:
        print("{id}: {name}".format(id=course["id"], name=course["name"]))
    print()

def get_student_mark(course):
    student_id = int(input("Enter student id: "))
    course_id = int(input("Enter course id: "))
    course_name = ""
    for c in course["courses"]:
        if c["id"] == course_id:
            course_name = c["name"]
            break
    if course_name == "":
        print("Unknown course!")
        print()
        return None
    for i, stud in enumerate(course["students"]):
        if stud["id"] == student_id:
            if course_name in stud["marks"].keys():
                print("Student id: {id} - {name}: {mark}".format(id=student_id, name=course_name, mark=stud["marks"][course_name]))
            else:
                print("Not updated!")
    print()

def option_prompt():
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
    
def main():
    course = {
        "no_students": 0,
        "students": [],
        "no_courses": 0,
        "courses": []
    }
    print("Student management program")
    while True:
        option = option_prompt()
        if option == 1:
            list_course(course)
        elif option == 2:
            list_student(course)
        elif option == 3:
            input_student(course)
        elif option == 4:
            input_course(course)
        elif option == 5:
            input_mark(course)
        elif option == 6:
            get_student_mark(course)
        elif option == 7:
            break
        else:
            print("Invalid option!")
    


main()