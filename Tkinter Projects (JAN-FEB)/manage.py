class Student:
    def __init__(self, name, roll_no, age, grade):
        self.name = name
        self.roll_no = roll_no
        self.age = age
        self.grade = grade

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def accept_details(self):
        name = input("Enter student name: ")
        roll_no = input("Enter roll number: ")
        age = input("Enter student age: ")
        grade = input("Enter student grade: ")
        student = Student(name, roll_no, age, grade)
        self.students.append(student)
        print("Student details entered successfully! ")

    def display_details(self):
        if not self.students:
            print("No student details available ")
            return 
        print("Student Details: ")
        for student in self.students:
            print(f"Name: {student.name}, Roll No: {student.roll_no}, Age: {student.age}, Grade: {student.grade}")

    
    def search_details(self):
        roll_no = input("Enter roll no. to search ")
        for student in self.students:
            if student.roll_no == roll_no:
                print("Student Found!")
                print(f"Name: {student.name}, Roll No: {student.roll_no}, Age: {student.age}, Grade: {student.grade}")
                return 
            print("Student not found with the given roll number. ")
    
    def delete_details(self):
        roll_no = input("Enter roll number to delete: ")
        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                print("Student details deleted successfully!")
                return
        print("Student not found with the given roll number.")

    def update_details(self):
        roll_no = input("Enter roll number to update: ")
        for student in self.students:
            if student.roll_no == roll_no:
                print("Update Student Details:")
                student.name = input("Enter updated name: ")
                student.age = input("Enter updated age: ")
                student.grade = input("Enter updated grade: ")
                print("Student details updated successfully!")
                return
        print("Student not found with the given roll number.")

    def menu(self):
        while True:
            print("\nStudent Management System Menu:")
            print("1. Accept Student Details")
            print("2. Display Student Details")
            print("3. Search Student Details")
            print("4. Delete Student Details")
            print("5. Update Student Details")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.accept_details()
            elif choice == '2':
                self.display_details()
            elif choice == '3':
                self.search_details()
            elif choice == '4':
                self.delete_details()
            elif choice == '5':
                self.update_details()
            elif choice == '6':
                print("Exiting...")
                break
            else:
                print("Invalid choice! Please choose again.")



if __name__ == "__main__":
    system = StudentManagementSystem()
    system.menu()