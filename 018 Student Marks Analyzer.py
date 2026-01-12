"""
 Challenge: Student Marks Analyzer

Create a Python program that allows a user to input student names along with their marks and then calculates useful statistics.

Your program should:
1. Let the user input multiple students with their marks (name + integer score).
2. After input is complete, display:
   - Average marks
   - Highest marks and student(s) who scored it
   - Lowest marks and student(s) who scored it
   - Total number of students

Bonus:
- Allow the user to enter all data first, then view the report
- Format output clearly in a report-style layout
- Prevent duplicate student names
"""

def collect_student_data():
    students = {}
    while True:
        name = input("Enter student name (or type 'done' to finish): ")
        if name.lower() == 'done':
            break
        if name in students:
            print("This student name already exists. Please enter a unique name.")
            continue
        try:
            marks = float(input(f"Enter marks for {name}: "))
            students[name] = marks
        except ValueError:
            print("Please enter a valid number for marks.")
    return students

def display_report(students):
    if not students:
        print("No student data to display.")
        return

    total_students = len(students)
    total_marks = sum(students.values())
    average_marks = total_marks / total_students
    highest_marks = max(students.values())
    lowest_marks = min(students.values())

    highest_scorers = [name for name, marks in students.items() if marks == highest_marks]
    lowest_scorers = [name for name, marks in students.items() if marks == lowest_marks]

    print("\n--- Student Marks Report ---")
    print(f"Total number of students: {total_students}")
    print(f"Average marks: {average_marks:.2f}")
    print(f"Highest marks: {highest_marks} by {', '.join(highest_scorers)}")
    print(f"Lowest marks: {lowest_marks} by {', '.join(lowest_scorers)}")
    print("-----------------------------")
    
def main():
    students = collect_student_data()
    display_report(students)
    
if __name__ == "__main__":
    main()
