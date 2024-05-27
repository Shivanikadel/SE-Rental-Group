"""
    Controller class for the MRS application
    ---------
    @Creation date: 15/05/2023
    @last modified: 20/05/2023
    @Author:Akanksha, Namrata, Shivani

	Team:12
    Team Members: Akanksha, Namrata, Shivani

"""


from application import Application
from boundary import Boundary
from property import Property
from watchlist import WatchList


class MonashRentalSpace:

    def fetch_registered_users(self):

        """open file that contains registered users and their passwords
        and store them in a list """

        user_pass_list = []

        try:

            reg_user_file = open("registered_users.txt", "r", encoding='Utf-8')

        except FileNotFoundError as error:
            print(error)
            return False

        except IOError as error:  # error excepted in case the file cannot be opened
            print(error)
            return False

        else:

            for line in reg_user_file:

                user_pass = dict()
                user_pass["username"] = line.split(";;;")[0]
                passwrd = line.split(";;;")[1].replace("\n", "")
                user_pass["password"] = passwrd

                user_pass_list.append(user_pass)

            return user_pass_list
        


def main():
    '''Defines menu and control logic for the application'''

    boundary = Boundary()
    mrs = MonashRentalSpace()
    property_list = Property.fetch_properties()
    user_pass_list = mrs.fetch_registered_users()

    mrs = "running"

    while mrs == "running":

        logged_in_user = boundary.login_screen(user_pass_list)
  
        if logged_in_user:
            logged_in = True
        else:
            continue

        while logged_in:

            user_input = boundary.home_screen(logged_in_user)

            if user_input == 1:

                Property.browse_properties(property_list)
                browsing = True

                while browsing:

                    user_input = boundary.property_screen()
                    if user_input == None:
                        continue
                    
                    if user_input == 1:

                        Property.browse_properties(property_list)
                        property_addr = input("\nEnter the property name (excluding suburb) whose details you want to see: ")
                        found = Property.show_property_details(property_addr, property_list)
                        if found:
                            choice = boundary.wishlist_input()

                            property = None
                            for item in property_list:
                                if property_addr in item.addr:
                                    property = item

                            if choice == 1:

                                WatchList.save_property(WatchList, logged_in_user, property)
                                continue

                            elif choice == 2:
                                user_input = boundary.application_input()
                                if user_input is not None and user_input == 'y' or user_input == 'Y':
                                    user_email = logged_in_user+"@student.monash.edu"
                                    employment_status = input("Enter employment status (unemployed/casual/part-time/full-time): ")
                                    estimated_hours = input("Enter the estimated hours: ")
                                    proof_of_income = input("Do you have proof of income? y/n : ")
                                    support_evidence= input("Do you have supporting evidence? y/n : ")
                                    application = Application(user_email, property_addr, employment_status, "Pending", estimated_hours, proof_of_income,
                               support_evidence)

                                    application.create_application()
                                else:
                                    continue

                            elif choice == 3:
                                Property.browse_properties(property_list)


                            elif choice == 4:
                                mrs = "stopped"
                                break

                            else:
                                print("Invalid Input. Please enter valid input from the given choices.")

                    elif user_input == 2:
                        browsing = False
                        break   

                    elif user_input == 3:
                        mrs = "stopped" 
                        exit()

                    else:
                        print("Invalid Input. Please enter valid input from the given choices.")

            elif user_input == 2:
                WatchList.show_watchlist(WatchList, logged_in_user)
                user_input = boundary.wishlist_menu()
                if user_input == None:
                    continue
                if user_input == 1:
                    property_address = input("Enter the property address to remove from the watchlist: ")
                    deleted = WatchList.delete_watchlist(WatchList, logged_in_user, property_address)
                    if deleted:
                        print("Property has been successfully deleted from watchlist.")
                elif input == 2:

                    break


            elif user_input == 3:
                logged_in = False
                print("You are logged out.")
                break

            elif user_input == 4:
                mrs = "stopped"
                exit()
                break

            else:
                print("Invalid Input. Please enter valid input from the given choices.")



if __name__ == '__main__':
    '''Calls the main function'''
    main()




