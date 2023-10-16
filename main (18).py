"""Implement a function called sort_students that takes a list of student objects as input and sorts the list based on their CGPA (Cumulative Grade Point Average) in descending order. Each student object has the following attributes: name (string), roll_number (string), and cgpa (float). Test the function with different input lists of students."""
class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa
def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students


# Sample list of student objects
students = [
    Student("Ezhil", "A101", 8.6),
    Student("Palani", "B102", 6.8),
    Student("Sakthi", "C103", 9.4),
    Student("Siva", "D104", 7.5),
]

# Sort the students by CGPA
sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")