class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.marks = {}

    def add_mark(self, student, mark):
        self.marks[student] = mark

class School:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self):
        id = input("Enter student id: ")
        name = input("Enter student name: ")
        dob = input("Enter student DoB: ")
        self.students.append(Student(id, name, dob))

    def add_course(self):
        id = input("Enter course id: ")
        name = input("Enter course name: ")
        self.courses.append(Course(id, name))

    def get_student(self, id):
        for student in self.students:
            if student.id == id:
                return student
        return None

    def get_course(self, id):
        for course in self.courses:
            if course.id == id:
                return course
        return None

    def list_students(self):
        for student in self.students:
            print(f"ID: {student.id}, Name: {student.name}, DoB: {student.dob}")

    def list_courses(self):
        for course in self.courses:
            print(f"ID: {course.id}, Name: {course.name}")

    def add_marks(self):
        course_id = input("Enter course id: ")
        course = self.get_course(course_id)
        if course:
            for student in self.students:
                mark = input(f"Enter mark for student {student.id}: ")
                course.add_mark(student, mark)

    def show_marks(self):
        course_id = input("Enter course id: ")
        course = self.get_course(course_id)
        if course:
            for student, mark in course.marks.items():
                print(f"Student ID: {student.id}, Mark: {mark}")

def main():
    school = School()

    while True:
        print("1. Add student")
        print("2. Add course")
        print("3. Add marks")
        print("4. List students")
        print("5. List courses")
        print("6. Show marks")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            school.add_student()
        elif choice == '2':
            school.add_course()
        elif choice == '3':
            school.add_marks()
        elif choice == '4':
            school.list_students()
        elif choice == '5':
            school.list_courses()
        elif choice == '6':
            school.show_marks()
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()