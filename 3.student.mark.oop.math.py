import math
import curses
import numpy as np

class Course:
    def __init__(self, course_id, name, credits):
        self.id = course_id
        self.name = name
        self.credits = credits

class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}
        self.gpa = 0.0

    def calculate_gpa(self, courses):
        """Calculates weighted average GPA using numpy arrays."""
        if not self.marks:
            self.gpa = 0.0
            return self.gpa
        
        marks_list = []
        credits_list = []
        
        for course_id, mark in self.marks.items():
            if course_id in courses:
                marks_list.append(mark)
                credits_list.append(courses[course_id].credits)
                
        if not credits_list or sum(credits_list) == 0:
            self.gpa = 0.0
        else:
            marks_array = np.array(marks_list)
            credits_array = np.array(credits_list)
            self.gpa = np.sum(marks_array * credits_array) / np.sum(credits_array)
        return self.gpa

class SchoolManagement:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_course(self, course_id, name, credits):
        self.courses[course_id] = Course(course_id, name, credits)

    def add_student(self, student_id, name, dob):
        self.students[student_id] = Student(student_id, name, dob)

    def add_mark(self, student_id, course_id, raw_score):
        """Rounds down student score to 1-digit decimal upon input using floor()."""
        rounded_score = math.floor(raw_score * 10) / 10.0
        if student_id in self.students and course_id in self.courses:
            self.students[student_id].marks[course_id] = rounded_score
            self.students[student_id].calculate_gpa(self.courses)

    def get_sorted_students(self):
        """Sorts student list by GPA descending."""
        student_list = list(self.students.values())
        student_list.sort(key=lambda s: s.gpa, reverse=True)
        return student_list


# --- Curses UI Design ---
def main_ui(stdscr):
    system = SchoolManagement()
    system.add_course("C1", "Python Programming", 3)
    system.add_course("C2", "Advanced Mathematics", 4)
    system.add_student("S1", "Alice Smith", "2004-05-12")
    system.add_student("S2", "Bob Jones", "2003-11-22")
    system.add_student("S3", "Charlie Brown", "2004-01-05")
    system.add_mark("S1", "C1", 16.78) # -> 16.7
    system.add_mark("S1", "C2", 14.55) # -> 14.5
    system.add_mark("S2", "C1", 18.99) # -> 18.9
    system.add_mark("S2", "C2", 19.21) # -> 19.2
    system.add_mark("S3", "C1", 12.34) # -> 12.3
    system.add_mark("S3", "C2", 15.67) # -> 15.6

    curses.curs_set(0)
    stdscr.clear()

    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        title = " STUDENT MARK MANAGEMENT SYSTEM (PW3) "
        stdscr.attron(curses.A_REVERSE | curses.A_BOLD)
        stdscr.addstr(1, max(0, (width - len(title)) // 2), title)
        stdscr.attroff(curses.A_REVERSE | curses.A_BOLD)

        stdscr.addstr(4, 4, f"{'ID':<8} {'Name':<18} {'DOB':<12} {'GPA (Descending)':<10}", curses.A_UNDERLINE)
        sorted_students = system.get_sorted_students()
        row = 6
        for idx, student in enumerate(sorted_students):
            if row >= height - 4: 
                break
            stdscr.addstr(row, 4, f"{student.id:<8} {student.name:<18} {student.dob:<12} {student.gpa:.2f}")
            row += 1

        footer = "Press [Q] to Exit / Marks rounded down via math.floor()"
        stdscr.addstr(height - 2, 4, footer, curses.A_DIM)
        stdscr.refresh()
        
        key = stdscr.getch()
        if key in [ord('q'), ord('Q')]:
            break

if __name__ == "__main__":
    curses.wrapper(main_ui)
