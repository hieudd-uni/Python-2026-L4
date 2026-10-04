import math


class Student:
    def __init__(self, i, n, d):
        self.id, self.name, self.dob = i, n, d
        self.marks = {}
        self.gpa = 0.0

    def calc_gpa(self, C):
        # Accept either a list of Course objects or a dictionary keyed by course id.
        if isinstance(C, dict):
            courses = C
        else:
            courses = {c.id: c for c in C}

        relevant_marks = {
            str(course_id): mark
            for course_id, mark in self.marks.items()
            if str(course_id) in courses
        }

        if not relevant_marks:
            self.gpa = 0.0
            return self.gpa

        weighted_total = 0.0
        total_credits = 0

        for course_id, mark in relevant_marks.items():
            course = courses[str(course_id)]
            weighted_total += float(mark) * int(course.credits)
            total_credits += int(course.credits)

        self.gpa = math.ceil((weighted_total / total_credits) * 100) / 100 if total_credits else 0.0
        return self.gpa