"""
    Class intro
    ---------
    @Creation date: 17/05/23
    @last modified: 20/05/23
    @Author: Akanksha Awadhiya

	Team: 12
    Team Members: Akanksha Awadhiya, Namrata, Shivani Kadel
	
"""

"""The Property class represents a MRS properties. 
It encapsulates information about various attributes of a property, such as its address,
cost per week, furnishing state, availability status, suburb, description,
inspection date and time, and listed date and time."""
class Property:
    """Defines property class"""

    def __init__(self, addr, cost_pw, furnish_state, avail_status,
                 suburb, description, inspection_date_time, listed_date_time):
        """Initialize the Property object with provided attributes"""


        self.addr = addr
        self.cost_pw = cost_pw
        self.furnish_state = furnish_state
        self.avail_status = avail_status
        self.suburb = suburb
        self.description = description
        self.inspection_date_time = inspection_date_time
        self.listed_date_time = listed_date_time

    def __str__(self):

        """Returns formatted string for Property object"""

        return (f"{self.addr};;;{self.cost_pw};;;{self.furnish_state};;;"
                f"{self.avail_status};;;{self.suburb};;;{self.description};;;"
                f"{self.inspection_date_time}")


    def fetch_properties():
        """Fetch all properties from properties.txt file and 
            stores them in a list"""

        property_list = []

        try:

            properties_file = open("properties.txt", "r", encoding='Utf-8')

        except FileNotFoundError as error:
            print(error)
            return False

        except IOError as error:  # error excepted in case the file cannot be opened
            print(error)
            return False

        else:

            for line in properties_file:
                # Loop through each line in the properties.txt file

                addr = line.split(";;;")[0]
                cost_pw = line.split(";;;")[1]
                furnish_state = line.split(";;;")[2]
                avail_status = line.split(";;;")[3]
                suburb = line.split(";;;")[4]
                description = line.split(";;;")[5]
                inspection_date_time = line.split(";;;")[6]
                listed_date_time = line.split(";;;")[7]

                # creating property object for each line in file properties.txt
                property_obj = Property(addr, cost_pw, furnish_state, avail_status,
                                        suburb, description, inspection_date_time, listed_date_time)

                property_list.append(property_obj)

            return property_list

    def browse_properties(property_list):
        """Function to search the properties"""

        print("\n\n********* PROPERTIES ***********\n")

        for prop in property_list:
            # Loop through each property object in the property_list
            print("Property: " + prop.addr + ", Suburb: " + prop.suburb)

    def show_property_details(property, property_list):
        """displays property details of the property entered by user"""

        property_found = False

        for prop in property_list:
            # Loop through each property object in the property_list to find a match with the entered property address

            if property == prop.addr:

                property_found = True

                print("\n")
                print(f"Property address: {prop.addr}")
                print(f"Weekly rent: {prop.cost_pw}")
                print(f"Furnishing: {prop.furnish_state}")
                print(f"Availability: {prop.avail_status}")
                print(f"Suburb: {prop.suburb}")
                print(f"Last inspection date and time: {prop.inspection_date_time}")
                print(f"Property listing date and time: {prop.listed_date_time}")
                print(f"Property description: \n{prop.description}\n")
            
        if not property_found:
            print("Property not found!")
            return False

        return True

