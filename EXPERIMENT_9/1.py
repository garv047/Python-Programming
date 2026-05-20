# 1.
class Student:
    def __init__(self, name, sap_id, marks):
        self.name = name
        self.sap_id = sap_id
        self.marks = marks

    def display(self):
        print(f"Name: {self.name} | SAP ID: {self.sap_id} | Marks: Physics={self.marks[0]}, Chemistry={self.marks[1]}, Maths={self.marks[2]}")

students = []

for i in range(3):
    print(f"Enter details for student {i+1}:")
    name = input("Name: ")
    sap_id = input("SAP ID: ")
    phy = int(input("Physics marks: "))
    chem = int(input("Chemistry marks: "))
    math = int(input("Maths marks: "))

    s = Student(name, sap_id, [phy, chem, math])
    students.append(s)

print("\n--- Student Details ---")
for s in students:
    s.display()
