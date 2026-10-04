from domain.course import Course
from domain.student import Student


def build_demo():
    courses = [
        Course("C1", "Python Programming", 3),
        Course("C2", "Advanced Mathematics", 4),
    ]

    student = Student("S1", "Alice Smith", "2004-05-12")
    student.marks = {"C1": 85, "C2": 90}
    student.calc_gpa(courses)

    return student, courses


def main():
    student, courses = build_demo()
    print(f"Student: {student.name} ({student.id})")
    print(f"DOB: {student.dob}")
    print(f"GPA: {student.gpa}")
    print("Courses:")
    for course in courses:
        print(f"- {course.id}: {course.name} ({course.credits} credits)")


if __name__ == "__main__":
    main()
