from gradebook import GradeBook
from student import Student
from course import Course

def main():
    grade_book = GradeBook()

    while True:
        print("\nGrade Book Application")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Register Student for Course")
        print("4. Calculate Ranking")
        print("5. Search by Grade")
        print("6. Generate Transcript")
        print("7. List All Students")
        print("8. Exit")
        choice = input("Choose an action: ")

        if choice == '1':
            email = input("Enter student email: ")
            names = input("Enter student names: ")
            student = Student(email, names)
            grade_book.add_student(student)
            print("Student added successfully.")

        elif choice == '2':
            name = input("Enter course name: ")
            trimester = input("Enter course trimester: ")
            credits = int(input("Enter course credits: "))
            course = Course(name, trimester, credits)
            grade_book.add_course(course)
            print("Course added successfully.")

        elif choice == '3':
            student_email = input("Enter student email: ")
            course_name = input("Enter course name: ")
            grade = float(input("Enter grade obtained: "))
            grade_book.register_student_for_course(student_email, course_name, grade)
            print("Student registered for course successfully.")

        elif choice == '4':
            ranking = grade_book.calculate_ranking()
            for rank, student in enumerate(ranking, start=1):
                print(f"{rank}. {student.names} - GPA: {student.GPA}")

        elif choice == '5':
            grade = float(input("Enter grade to search for: "))
            students = grade_book.search_by_grade(grade)
            for student in students:
                print(f"{student.names} - GPA: {student.GPA}")

        elif choice == '6':
            student_email = input("Enter student email: ")
            transcript = grade_book.generate_transcript(student_email)
            if transcript:
                print(f"Transcript for {transcript['names']} (Email: {transcript['email']})")
                for course in transcript['courses_registered']:
                    print(f"Course: {course['course'].name}, Grade: {course['grade']}, Credits: {course['credits']}")
                print(f"GPA: {transcript['GPA']}")
            else:
                print("Student not found.")

        elif choice == '7':
            grade_book.list_students() 

        elif choice == '8':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


