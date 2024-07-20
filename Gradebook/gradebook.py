from student import Student
from course import Course

class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []

    def add_student(self, student):
        self.student_list.append(student)

    def add_course(self, course):
        self.course_list.append(course)

    def register_student_for_course(self, student_email, course_name, grade):
        student = next((s for s in self.student_list if s.email == student_email), None)
        course = next((c for c in self.course_list if c.name == course_name), None)
        if student and course:
            student.register_for_course(course, grade)
            student.calculate_GPA()

    def calculate_ranking(self):
        return sorted(self.student_list, key=lambda s: s.GPA, reverse=True)

    def search_by_grade(self, grade):
        return [student for student in self.student_list if any(course['grade'] == grade for course in student.courses_registered)]

    def generate_transcript(self, student_email):
        student = next((s for s in self.student_list if s.email == student_email), None)
        if student:
            return {
                'names': student.names,
                'email': student.email,
                'GPA': student.GPA,
                'courses_registered': student.courses_registered
            }
    
    def list_students(self):
        print("\nList of Students:")
        for student in self.student_list:
            print(f"Name: {student.names}, Email: {student.email}, GPA: {student.GPA}")

