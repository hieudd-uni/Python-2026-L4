from abc import ABC, abstractmethod

def input_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
        except ValueError:
            pass
        print("Please enter a non-negative integer.")

class Entity(ABC):
    ""Common interface: every entity can read itself from input and list itself.""

    def __init__(self, entity_id="", name=""):
        self._id = entity_id
        self._name = name

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @abstractmethod
    def input(self):
        ...

    @abstractmethod
    def list(self):
        ...

class Student(Entity):
    def __init__(self, student_id="", name="", dob=""):
        super().__init__(student_id, name)
        self.__dob = dob          # private

    @property
    def dob(self):
        return self.__dob

    def input(self):
        self._id = input("  Student id: ").strip()
        self._name = input("  Student name: ").strip()
        self.__dob = input("  Student DoB (dd/mm/yyyy): ").strip()

    def list(self):
        print(f"  {self._id} - {self._name} (DoB: {self.__dob})")

class Course(Entity):
    def __init__(self, course_id="", name=""):
        super().__init__(course_id, name)
        self.__marks = {}         # private: student_id -> mark

    def input(self):
        self._id = input("  Course id: ").strip()
        self._name = input("  Course name: ").strip()

    def list(self):
        print(f"  {self._id} - {self._name}")

    def set_mark(self, student_id, mark):
        self.__marks[student_id] = mark

    def get_mark(self, student_id):
        return self.__marks.get(student_id)

    def input_marks(self, students):
        print(f"Entering marks for {self._name}:")
        for s in students:
            while True:
                try:
                    self.set_mark(s.id, float(input(f"  Mark for {s.name} ({s.id}): ")))
                    break
                except ValueError:
                    print("  Please enter a number.")

    def list_marks(self, students):
        print(f"Marks for {self._name}:")
        for s in students:
            mark = self.get_mark(s.id)
            print(f"  {s.id} - {s.name}: {mark if mark is not None else 'N/A'}")

class MarkManager:
    def __init__(self):
        self.__students = []
        self.__courses = []

    def __input_many(self, cls, label, target):
        n = input_int(f"Number of {label}s: ")
        for i in range(n):
            print(f"{label.capitalize()} {i + 1}:")
            obj = cls()
            obj.input()
            target.append(obj)

    @staticmethod
    def __list_all(title, items):
        print(f"{title}:")
        for item in items:
            item.list()

    def __select_course(self):
        self.__list_all("Courses", self.__courses)
        cid = input("Select a course id: ").strip()
        return next((c for c in self.__courses if c.id == cid), None)

    def input_students(self):
        self.__input_many(Student, "student", self.__students)

    def input_courses(self):
        self.__input_many(Course, "course", self.__courses)

    def input_marks(self):
        if not self.__courses or not self.__students:
            print("Need at least one course and one student first.")
            return
        course = self.__select_course()
        if course is None:
            print("Course not found.")
            return
        course.input_marks(self.__students)

    def list_courses(self):
        self.__list_all("Courses", self.__courses)

    def list_students(self):
        self.__list_all("Students", self.__students)

    def show_marks(self):
        course = self.__select_course()
        if course is None:
            print("Course not found.")
            return
        course.list_marks(self.__students)

    def run(self):
        self.input_students()
        self.input_courses()
        menu = {
            "1": ("Input marks for a course", self.input_marks),
            "2": ("List courses", self.list_courses),
            "3": ("List students", self.list_students),
            "4": ("Show student marks for a course", self.show_marks),
            "0": ("Exit", None),
        }
        while True:
            print("\n--- Menu ---")
            for key, (label, _) in menu.items():
                print(f"{key}. {label}")
            choice = input("Choice: ").strip()
            if choice == "0":
                break
            if choice in menu:
                menu[choice][1]()
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    MarkManager().run()