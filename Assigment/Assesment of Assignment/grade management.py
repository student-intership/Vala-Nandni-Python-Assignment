def display_menu():
    """Displays the main menu of the system."""
    print("\nGrade Management System")
    print("1. Student Grade")
    print("2. View All Grades")
    print("3. Calculate Average Grade")
    print("4. Get Grade Feedback")
    print("5. Exit")

def student_grade(students_grades):
    """Adds a student's name and grade to the system."""
    name = input("Enter student name: ")
    while True:
        try:
            grade = float(input(f"Enter grade for {name}: "))
            if 0 <= grade <= 100:
                break
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a numeric value for the grade.")
    students_grades[name] = grade
    print(f"Grade for {name} added successfully!")

def view_all_grades(students_grades):
    """Displays all students and their grades."""
    if not students_grades:
        print("No student grades available.")
    else:
        print("\nStudent Grades:")
        for name, grade in students_grades.items():
            print(f"{name}: {grade}")

def calculate_average_grade(students_grades):
    """Calculates the average grade of all students."""
    if not students_grades:
        print("No student grades available.")
    else:
        average = sum(students_grades.values()) / len(students_grades)
        print(f"\nAverage grade of all students: {average:.2f}")

def get_grade_feedback(students_grades):
    """Gives feedback based on the average grade."""
    if not students_grades:
        print("No student grades available.")
    else:
        average = sum(students_grades.values()) / len(students_grades)
        if average >= 90:
            print("Feedback: Excellent performance!")
        elif 70 <= average < 90:
            print("Feedback: Good job!")
        elif 50 <= average < 70:
            print("Feedback: You need improvement.")
        else:
            print("Feedback: Poor performance. Needs serious improvement.")

def main():
    students_grades = {}  # Dictionary to store student names and grades

    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            student_grade(students_grades)
        elif choice == "2":
            view_all_grades(students_grades)
        elif choice == "3":
            calculate_average_grade(students_grades)
        elif choice == "4":
            get_grade_feedback(students_grades)
        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose a valid option (1-5).")

if __name__ == "__main__":
    main()
