from contestant import Contestant

class User_interface:
    def __init__(self):
        pass

    def contestant_info(self):
        fname = input("Please enter your first name: ")
        lname = input("Please enter you last name: ")
        email = input("Please enter you email: ")
        registration = int(input("Please enter a four digit number: "))

        new_contestant = Contestant(fname, lname, email, registration)
        return new_contestant

    def get_manager_type(self):
        manager_type = input("Select a data type to order Sweepstakes (stack or queue): ")
        return manager_type

    def get_sweepstakes_info(self):
        prize = input("Please enter a prize")
        return prize

