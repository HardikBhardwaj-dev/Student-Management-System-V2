# LEVEL 1 (creating a class and printing the menu)


class student_management_system_v2:
    def __init__(self):
        pass
    def menu(self):
        print("====STUDENT MANAGEMENT SYSTEM====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Exit")
        print()
        print()

        user_choice= int(input("Enter the number according to your choice: "))   # Exception handling will be added if the given input is not integer

        
sms_v2= student_management_system_v2()
sms_v2.menu()