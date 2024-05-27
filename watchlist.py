"""
    Class for saving watchlisted properties for tenants of MRS application.
    ---------
    @Creation date: 15/05/2023
    @last modified: 20/05/2023
    @Author: Shivani, Namrata

	Team:12
    Team Members: Akanksha, Namrata, Shivani

"""

""" NOTE: Importing datetime is used to import the built-in datetime module, 
this provides WatchList for working with dates and times."""

import datetime

watchlisted_properties = []

class WatchList:
    """Watchlist params"""
    def __init__(self, property_address, listed_DateAndTime):
        self.property_address = property_address
        self.listed_DateAndTime = listed_DateAndTime
        self.watchlist_DateAndTime = datetime.datetime.now()


    def check_watchlist(self, tenant, property_address):
        """
            Retrieves the property from the watchlist.

            Returns:
                str: The property addresss if available, None otherwise.
            """
        for object in watchlisted_properties:
            if property_address in object.addr:
                return True

            elif property_address not in object.addr:
                f = open("watchlist.txt", "r")
                lines = f.readlines()
                for line in lines:
                    if tenant in line:
                        if property_address in line:
                            return True
            else:
                return False


    def save_property(self, tenant, property_obj):
        """
             Saves the specified property to the watchlist with the associated date and time information.

             Args:
                 property_obj (object of Property class): The instance of the property to add to the watchlist.

             Returns:
                 bool: True if the property is successfully saved (not already in the watchlist),
                       False if the property is already in the watchlist.
             """
        if property_obj is not None:
            if WatchList.check_watchlist(WatchList, tenant, property_obj.addr):
                print("Property is already in the watchlist.")
                return 0
            watchlisted_properties.append(property_obj)
            f = open("watchlist.txt", "a")
            f.write(f"{tenant}: {str(property_obj)}: {datetime.datetime.now()}\n")
            f.close()
            print("Property has been added.")

    def delete_watchlist(self, logged_in_user, property_address):
        """
        Deletes the specified property from the watchlist.

        Args:
            property_address (str): The address of the property to delete.

        Returns:
            bool: True if the property is successfully deleted, False otherwise.
        """
        new_lines = []
        f = open("watchlist.txt", "r+")
        lines = f.readlines()
        found = False

        for line in lines:
            if property_address in line and logged_in_user in line:
                found = True
                continue
            else:
                new_lines.append(line)

        if found is not True:
            print("Property not found in the watchlist.")
            return False

        f = open("watchlist.txt", "w")
        f.write(" ")
        f.writelines(new_lines)

        return True

    def show_watchlist(self, tenant):
        """
               Shows all watchlisted properties.

        """

        i = 1
        watchlist_property_list = []
        watchlist_time = []
        f = open("watchlist.txt", "r", encoding='Utf-8')
        lines = f.readlines()
        for line in lines:
            if tenant in line:
                watchlist_property_list.append(line.split(": ")[1].split(";;;")[0])
                watchlist_time.append(line.split(";;;")[-1])

        if watchlist_property_list:
            print("\n\n**************************WATCHLIST*************************\n")
            for item in watchlist_property_list:
                print(f"{i}: {item}: {watchlist_time[i-1]}")
                i = i + 1
            print("************************************************************\n")

        else:
            print("No properties have been added to watchlist yet.\n")
