from FTmodels import Student,Course

courses_list = []
student_list = []



def get_courses_details(courses):
    print("ID\t\tNAME\t\tClass")
    for course in courses:
        course.get_course_details()

def get_students_details(students):
    for student in students:
        print("ID\t\tNAME\t\tClass")
        print(student.get_student_details())


def find_student(student_id , students):
    index = 0
    for student in students:
        if student.student_id == student_id:
            return index
        index += 1
    return -1


def find_course(course_id, courses):
    index = 0
    for course in courses:
        if course.course_id == course_id:
            return index
        index += 1
    return -1


while True:

    print("----------Select Choice Please-------------")
    x = int(input(" 1- Add New student \n 2- Remove student \n 3- Edit student \n"
                  " 4- Display All Students \n 5- Create New Course  \n 6- Add course to Student \n 0- Exit \n Enter: "))
    if x == 1:
        student_name = input("Enter Student name : ")

        while True:

            student_class = input("Select Student Class [ A - B - C ]")
            if student_class in ("A", "B", "C"):
                break

        student_id = len(student_list) + 1
        student = Student(student_id,student_name,student_class)
        student_list.append(student)
        print("Student Saved Successfully..... ")
    elif x == 2:
        get_students_details(student_list)
        student_id = int(input("Enter student id you want to delete :"))
        student_index = find_student(student_id,student_list)
        if student_index == -1:
            print("student not exist ....")
        else:
            student_list.pop(student_index)
            print('deleted successfully ..... ')
            get_students_details(student_list)

        # for student in student_list:
        #     if student.student_id == student_id:
        #         student_list.pop(student_list.index(student))
        #         print('deleted successfully ')
        #         break
    elif x == 3:
        get_students_details(student_list)
        student_id = int(input("Enter student id :"))
        student_index = find_student(student_id, student_list)
        if student_index == -1:
            print("student not exist ....")
        else:
            student_name = input("Enter Student name : ")
            while True:
                student_class = input("Select Student Class [ A - B - C ]")
                if student_class in ("A", "B", "C"):
                    break
            student_list[student_index].student_name = student_name
            student_list[student_index].student_class = student_class
            print("student updated successfully....")


    elif x == 4:
        get_students_details(student_list)

        # print("------------------------------------")

        # print("Student ID \t\t\t Student Name \t\t\t  Student Class")
        # for i in student_list:
        #     print(
        #         f" {i.student_id} \t\t\t\t\t | {i.student_name} \t\t\t\t\t\t {i.student_class}")
    elif x == 5:
        course_name = input("Enter Course name : ")

        while True:
            course_class = input("Select Course Class [ A - B - C ]")
            if course_class in ["A", "B", "C"]:
                break
        course_id = len(courses_list) + 1
        course = Course(course_id,course_name,course_class)
        courses_list.append(course)
        print("Course saved successfully.....")

    elif x == 6:
        get_courses_details(courses_list)
        student_id = int(input("Enter student ID : "))
        student_index = find_student(student_id,student_list)
        if student_index == - 1 :
            print("student not exist ...")
        else:
            course_id = int(input("Enter course ID : "))
            course_index = find_course(course_id,courses_list)
            if course_index == -1:
                print("course not exist")
            else:
                student_list[student_index].enroll_course(courses_list[course_index])
    elif x == 0:
        exit()