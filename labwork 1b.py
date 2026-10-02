def input_students():
    students = []

    number = int(input("Enter number of students: "))

    for i in range(number):
        print(f"\nStudent {i + 1}")

        student_id = input("ID: ")
        name = input("Name: ")
        dob = input("Date of birth (DD/MM/YYYY): ")

        student = {
            "id": student_id,
            "name": name,
            "dob": dob
        }

        students.append(student)

    return students


def input_courses():
    courses = []

    number = int(input("\nEnter number of courses: "))

    for i in range(number):
        print(f"\nCourse {i + 1}")

        course_id = input("Course ID: ")
        name = input("Course name: ")

        course = {
            "id": course_id,
            "name": name
        }

        courses.append(course)

    return courses


def input_marks(students, courses, marks):
    if not courses:
        print("No courses available.")
        return

    if not students:
        print("No students available.")
        return

    list_courses(courses)

    course_id = input("\nEnter course ID: ")

    # Check whether the course exists
    selected_course = None

    for course in courses:
        if course["id"] == course_id:
            selected_course = course
            break

    if selected_course is None:
        print("Course not found.")
        return

    print(f"\nEntering marks for: {selected_course['name']}")

    for student in students:
        while True:
            try:
                mark = float(
                    input(f"Enter mark for {student['name']}: ")
                )

                if 0 <= mark <= 100:
                    break

                print("Mark must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

        if student["id"] not in marks:
            marks[student["id"]] = {}

        marks[student["id"]][course_id] = mark

    print("Marks entered successfully.")


def list_students(students):
    print("\n===== STUDENTS =====")

    if not students:
        print("No students available.")
        return

    for student in students:
        print(
            f"ID: {student['id']} | "
            f"Name: {student['name']} | "
            f"DoB: {student['dob']}"
        )


def list_courses(courses):
    print("\n===== COURSES =====")

    if not courses:
        print("No courses available.")
        return

    for course in courses:
        print(
            f"ID: {course['id']} | "
            f"Name: {course['name']}"
        )


def show_marks(students, courses, marks):
    if not courses:
        print("No courses available.")
        return

    list_courses(courses)

    course_id = input("\nEnter course ID: ")

    selected_course = None

    for course in courses:
        if course["id"] == course_id:
            selected_course = course
            break

    if selected_course is None:
        print("Course not found.")
        return

    print(f"\n===== MARKS: {selected_course['name']} =====")

    for student in students:
        student_marks = marks.get(student["id"], {})
        mark = student_marks.get(course_id, "Not entered")

        print(
            f"ID: {student['id']} | "
            f"Name: {student['name']} | "
            f"Mark: {mark}"
        )


def main():
    students = []
    courses = []
    marks = {}

    while True:
        print("\n========== STUDENT MARK MANAGEMENT ==========")
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks")
        print("4. List students")
        print("5. List courses")
        print("6. Show student marks for a course")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            students = input_students()

        elif choice == "2":
            courses = input_courses()

        elif choice == "3":
            input_marks(students, courses, marks)

        elif choice == "4":
            list_students(students)

        elif choice == "5":
            list_courses(courses)

        elif choice == "6":
            show_marks(students, courses, marks)

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
