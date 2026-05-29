# 2.
class Student:
    def __init__(self, name, sap_id, marks):
        self.name = name
        self.sap_id = sap_id
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, SAP ID: {self.sap_id}, Marks: {self.marks}")

    def find_marks_percentage(self):
        percentage = sum(self.marks) / 3
        return percentage

    def display_result(self):
        if all(m > 40 for m in self.marks):
            return "Pass"
        else:
            return "Fail"

def find_class_average(student_list):
    total_marks = sum(sum(s.marks) for s in student_list)
    total_subjects = len(student_list) * 3
    return total_marks / total_subjects

n = int(input("Enter number of students: "))
students = []

for i in range(n):
    print(f"\nEnter details for Student {i+1}:")
    name = input("Name: ")
    sap = input("SAP ID: ")
    p = int(input("Physics marks: "))
    c = int(input("Chemistry marks: "))
    m = int(input("Maths marks: "))
    students.append(Student(name, sap, [p, c, m]))

print("\n--- Student Records ---")
for s in students:
    s.display()
    print(f"Percentage: {s.find_marks_percentage():.2f}%")
    print(f"Result: {s.display_result()}")
    print("-" * 20)

if students:
    print(f"\nOverall Class Average: {find_class_average(students):.2f}")
