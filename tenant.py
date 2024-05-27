"""
    Tenant class for the tenants of MRS application.
    ---------
    @Creation date: 15/05/2023
    @last modified: 20/05/2023
    @Author:Namrata

	Team:12
    Team Members: Akanksha, Namrata, Shivani

"""

class Tenant:

    def __init__(self, first_name, last_name, email_id, gender, mobile_num, password, preferred_rent_cost, preferred_suburb, wishlisted_properties = ""):

        """Tenant params"""

        self.first_name = first_name
        self.last_name = last_name
        self.email_id = email_id
        self.gender = gender
        self.mobile_num = mobile_num
        self.password = password
        self.preferred_rent_cost = preferred_rent_cost
        self.preferred_suburb = preferred_suburb
        self.wishlisted_properties = wishlisted_properties
        self.write_to_txt(str(self))

    def __str__(self):

        """returns formatted string for Tenant object"""

        return (
            f"{self.first_name};;;{self.last_name};;;{self.email_id};;;{self.gender};;;{self.mobile_num};;;"
            f"{self.password};;;{self.preferred_rent_cost};;;{self.preferred_suburb};;;{self.wishlisted_properties}")

    def write_to_txt(self, record):

        """ Writes the tenant record to text file"""

        f = open("tenant.txt", "a", encoding='Utf-8')
        f.write(record)
        f.close()
