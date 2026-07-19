import csv

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

        try:
            user_choice= int(input("Enter the number according to your choice: "))   # Exception handling will be added if the given input is not integer
            if user_choice>=1 and user_choice<7:
                return user_choice
            else:
                print("Enter the option from 1-6")
                return self.menu()
        except ValueError:
            print("Must be an integer input ex: 1,2,3..")
            return self.menu()

        



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
            self.delete_student()
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
                pass
    
    def add_student(self):
        while True:
            try:
                Roll_no= int(input("Enter the Roll No of the student: "))
                break
            except ValueError:
                print("Roll no of the student can only be in integers ex: 1,2,3,4....")

        Name= input("Enter the name of the student: ")
        
        while True:
            try:
                Marks= int(input("Enter the Marks of the student: "))
                break
            except ValueError:
                print("Marks of the student can only be in integer ex: 1,2,3,4....")

        student_details= Student(Roll_no,Name,Marks) # LEVEL 5 END
        self.students.append(student_details)
        self.save_student()
        
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
            while True:
                try:
                    roll_number_to_be_searched= int(input("Enter the roll number of the student to search: "))
                    break
                except ValueError:
                    print("Roll no of the student can only be in integers ex: 1,2,3,4....")
            for stu in self.students:
                if roll_number_to_be_searched== stu.Roll_no:
                    print(stu.Roll_no)
                    print(stu.Name)
                    print(stu.Marks)
                    break
            else:
                print("No student with this roll number found in records.")
            

    def update_student(self):
        if len(self.students)==0:
            print("No student found in the records.")
        else:
            while True:
                try:
                    roll_number_to_be_updated= int(input("Enter the roll number of the student to update: "))
                    break
                except ValueError:
                    print("Roll no of the student can only be in integers ex: 1,2,3,4....")
            for stu in self.students:
                if roll_number_to_be_updated==stu.Roll_no:
                    updated_name= input("Enter the new name of studnet: ")
                    while True:
                        try:
                            updated_marks = int(input("Enter the new marks of the student: "))
                            break
                        except ValueError:
                            print("Marks should be integer only")
                    stu.Marks= updated_marks
                    stu.Name= updated_name
                    print("Student updated successfully.")
                    self.save_student()
                    break
            else:
                print("No student with this roll number found in records.")



    def delete_student(self):
        if len(self.students)==0:
            print("No student found in the records.")
        else:
            while True:
                try:
                    roll_number_to_be_deleted= int(input("Enter the roll number of the student whose record you want to delete: "))
                    break
                except ValueError:
                    print("Roll no of the student can only be in integers ex: 1,2,3,4....")
            for stu in self.students:
                if roll_number_to_be_deleted== stu.Roll_no:
                    self.students.remove(stu)
                    print("Student deleted successfully.")
                    self.save_student()
                    break
            else:
                print("No student with this roll number found in records.")

    def save_student(self):
        with open("xyz.csv","w",newline="") as file:
            writer= csv.writer(file)
            for student in self.students:
                writer.writerow([student.Roll_no,student.Name,student.Marks])

    def load_student(self):
        with open("xyz.csv", "r", newline="") as load_file:
            reader = csv.reader(load_file)

        for student in reader:
            Roll_no = int(student[0])
            Name = student[1]
            Marks = int(student[2])

            student_object = Student(Roll_no, Name, Marks)
            self.students.append(student_object)


sms_v2 = student_management_system_v2()

while sms_v2.Program_running:
    user_choice_in_menu = sms_v2.menu()
    sms_v2.choice_handle(user_choice_in_menu)