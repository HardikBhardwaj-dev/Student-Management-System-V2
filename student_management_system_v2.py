class Student:
    def __init__(self,Roll_no,Name,Marks):
        self.Roll_no=Roll_no
        self.Name=Name
        self.Marks=Marks

class student_management_system_v2:
    def __init__(self):
        self.students= []
        self.Program_running= True

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
        return user_choice



    def choice_handle(self,user_choice):
        


        if user_choice== 1:
            print("You have selected to add a student.")
            self.add_student()
        elif user_choice== 2:
            print("You have selected to view students.")
            self.view_student()
        elif user_choice== 3:
            print("You have selected to update a student.")
            self.update_student()
        elif user_choice== 4:
            print("You have selected to delete a student.")
        elif user_choice== 5:
            print("You have selected to search for a student.")
            self.search_student()
        elif user_choice== 6:
            print("You have selected to exit.")
            print("Are you sure you want to Exit?")
            print("Press Y for 'yes' and N for 'no'")
            exit_choice= input("Y or N: ")
            if exit_choice.upper()=='Y':
                print("Exiting the application....")
                self.Program_running=False
            else:
                # sms_v2.menu()
    
    def add_student(self):
        Roll_no= int(input("Enter the Roll No of the student: "))
        Name= input("Enter the name of the student: ")
        Marks= int(input("Enter the Marks of the student: "))

        student_details= Student(Roll_no,Name,Marks) # LEVEL 5 END
        self.students.append(student_details)
        
    def view_student(self):
        if len(self.students)==0:
            print("No students found in the records.")
        else:
            for stu in self.students:
                print(stu.Roll_no)
                print(stu.Name)
                print(stu.Marks)
    
    def search_student(self):
        if len(self.students)==0:
            print("No student found in the records.")
        else:
            roll_number_to_be_searched= int(input("Enter the roll number of the student to search: "))
            for stu in self.students:
                if roll_number_to_be_searched== stu.Roll_no:
                    print(stu.Roll_no)
                    print(stu.Name)
                    print(stu.Marks)
                    break

    def update_student(self):
        if len(self.students)==0:
            print("No student found in the records.")
        else:
            roll_number_to_be_updated= int(input("Enter the roll number of the student to update"))
            for stu in self.students:
                if roll_number_to_be_updated==stu.Roll_no:
                    updated_name= input("Enter the new name of studnet: ")
                    updated_marks= int(input("Enter the new marks of the student: "))
                    stu.Marks= updated_marks
                    stu.Name= updated_name
                    break
                    




        
sms_v2 = student_management_system_v2()

while sms_v2.Program_running:
    user_choice_in_menu = sms_v2.menu()
    sms_v2.choice_handle(user_choice_in_menu)


