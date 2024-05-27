"""
    Boundary class for the MRS application
    ---------
    @Creation date:15/05/2023
    @last modified:
    @Author:Akanksha, Namrata

	Team:12
    Team Members: Akanksha, Namrata, Shivani

"""

import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]student.monash.edu'


class Boundary:

    def check_str(self, input):

        if isinstance(input, str):
            return True

        else:
            print("The input is not valid. Please try again.")
            return False

    def check_num(input):

        if input.isdigit():
            return True

        else:
            print("The input is not valid. Please try again.")
            return False

    def check_email(self, input):

        if (re.search(regex, input)):
            return True

        else:
            return False


    def login_screen(self, user_pass_list):
        """Displays login screen to tenant"""

        print(
            """\n\n********* LOGIN INTO MRS ***********"""
        )

        username = input("\nEnter Username: ")

        if self.check_email(username):

            user_found = False
            for user_pass in user_pass_list:

                if user_pass["username"] == username:
                    user_found = True

                    password = input("Enter Password: ")
                    # check corresponding password

                    if user_pass["password"] == password:
                        print("\nLogin Successful.")
                        return username.split("@")[0]
                    
                    else:
                        print("Password is incorrect")
                        return None

            if not user_found:
                    print("\nUser is incorrect ")
                    return None
            
            else:
                print("The entered username or password is invalid. Please try again.")
                return None
        else:
            print("\nInput is not an email address of domain monash.edu.\n" +\
                  "Please enter your monash student email address.")
            return None


    def home_screen(self,logged_in_user):
        """Displays home screen to tenant"""

        print(
            f'\n\n********* HI {logged_in_user.upper()}, WELCOME TO MRS! ***********')
        print(
            """
----------------------------
1. Browse properties
2. See wishlisted properties
3. Logout
4. Exit
----------------------------
"""
        )

        user_input = input("Please enter your choice: ")
        if (Boundary.check_num(user_input)):
            user_input = int(user_input)

        return user_input

    def property_screen(self):

        """Displays the screen to show properties and
        allows user to input the property whose detail he or she
        wants to see"""

        print(
            """
------------------------
1. See property details
2. Go back to Main Menu
3. Exit
------------------------
"""    )

        user_input = input("Please enter your choice: \n")
        if (Boundary.check_num(user_input)):
            user_input = int(user_input)
            return user_input
        return None

    def wishlist_menu(self):
        print("""
--------------WISHLIST MENU--------------
1. Delete properties
2. Go back
-----------------------------------------
""")
        user_choice = input("Enter your choice: ")
        if Boundary.check_num(user_choice):
            user_input = int(user_choice)
            return user_input
        else:
            return None



    def wishlist_input(self):
        """Takes user input for choice of actions"""

        print("""
---------------------------------------
1. Wishlist this property
2. Submit application for this property
3. Go back
4. Exit
---------------------------------------

                """)

        user_input = input("Please enter your choice: ")
        if (Boundary.check_num(user_input)):
            user_input = int(user_input)

        return user_input
    def application_input(self):

        """takes input for create application"""

        user_input = input("""
Create application.
NOTE: Your personal information such as email and phone number will be shared with the owner.
Enter 'y' to proceed:  
""")
                           
        if Boundary.check_str(Boundary, user_input):
            return user_input
        return None

