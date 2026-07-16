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
        return user_choice

# LEVEL 2 AND 3

    def choice_handle(self,user_choice):
        


        if user_choice== 1:
            print("You have selected to add a student.")
        elif user_choice== 2:
            print("You have selected to view students.")
        elif user_choice== 3:
            print("You have selected to update a student.")
        elif user_choice== 4:
            print("You have selected to delete a student.")
        elif user_choice== 5:
            print("You have selected to search for a student.")
        elif user_choice== 6:
            print("You have selected to exit.")
            print("Are you sure you want to Exit?")
            print("Press Y for 'yes' and N for 'no'")
            exit_choice= input("Y or N: ")
            if exit_choice.upper()=='Y':
                print("Exiting the application....")
            else:
                sms_v2.menu()
        
        

        
sms_v2= student_management_system_v2()
user_choice_in_menu= (sms_v2.menu())
sms_v2.choice_handle(user_choice_in_menu)