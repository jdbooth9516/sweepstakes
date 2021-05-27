#from contestant import Contestant


class User_interface:
    def __init__(self):
        self.first = ''
        self.last = ' '
        self.email = ''
        self.registration = ''

    def main_menu(self):
        print("""Welcome to the main menu \n\t 
        press -1- to create a contest\n\t 
        press -2- to add a contestant\n\t
        press -3- to pick a winner\n\t
        press -4- to quit program""")
        choice = int(input("select a option: "))

        return choice
 
    def contestant_info(self, contest_name):
        print(f"Enter contestand for the {contest_name} sweepstake\n")
        self.first = input("Please enter contestant's first name: ")
        self.last = input("Please enter contestant's last name: ")
        self.email = input("Please enter contestant's email: ")
        self.registration = int(input("Please enter contestant's four digit registration number: "))

    def get_manager_type(self):
        manager_type = input("Select a data type to order Sweepstakes (stack or queue): ")
        return manager_type

    def get_sweepstakes_info(self):
        prize = input("Please enter a prize: ")
        return prize

    def finished_entry(self):
        finished = input("Would anyone else like to join the sweepstake (y/n): ")
        if finished == 'y':
            return False
        else: 
            return True

    def finished_sweepstakes(self):
        entry_finished = input("Would you like to add another sweepstake (y/n): ")
        if entry_finished == "n":
            return True

    def finished_contest(self):
        contest_finished = input('Would you like to run another sweepstake (y/n): ')
        if contest_finished == "n": 
            return True


    def close(self):
        print("Registration has closed stand by for the winner.")


    def recieve_message(self, first_name):
        print(f"{first_name} has recieved the message")

    def recieve_winner(self, first_name):
        print(f"{first_name} has recieved prize information")



