"""
    Class intro
    ---------
    @Creation date:18/05/2023
    @last modified:
    @Author:Shivani

	Team:12
    Team Members: Akanksha, Namrata, Shivani

"""
from property import Property

"""This class represents a rental application 
submitted by a tenant for a specific property. 
It provides attributes and methods to manage and 
access information related to the application."""
class Application:
    def __init__(self, tenant_email, property_addr, employment_status,app_status,
                 estimated_hours, proof_of_income, support_evidence):
        
        # Initialize the Application object with tenant email and property object
        self.employment_status = employment_status
        self.estimated_hours = estimated_hours
        self.proof_of_income = proof_of_income
        self.support_evidence = support_evidence
        self.tenant_email = tenant_email
        self.property_addr = property_addr
        self.application_status = app_status

    def __str__(self):

        """returns formatted string for Tenant object"""

        return f"{self.tenant_email};;;{self.property_addr};;;{self.employment_status};;;{self.application_status};;;{self.estimated_hours};;;{self.proof_of_income};;;{self.support_evidence};;;"

    def create_application(self):

        # Find the property object based on the property address from the property_list

        app_file = open("application.txt", "r+",encoding='Utf-8')

        lines = app_file.readlines()

        found = False

        for line in lines:
            if self.tenant_email in line and self.property_addr in line:
                found = True
                print("\nYou have already applied for this property")
                break

        if not found:
            app_file.write(str(self))
            print("\nApplication created.")
