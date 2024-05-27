"""
    Class for Feature 4 (Utilities of MRS system).
    This is just a dummy class and will not be used in the main logic.
    ---------
    @Creation date:15/05/2023
    @last modified:
    @Author:Namrata

	Team:12
    Team Members: Akanksha, Namrata, Shivani

"""


class Utility:

    def __init__(self, weekly_income, weekly_rent):
        self.weekly_income = weekly_income
        self.weekly_rent = weekly_rent

    def __str__(self):

        """returns formatted string for Utility object"""

        return (
            f"{self.weekly_income};;;{self.weekly_rent}")
