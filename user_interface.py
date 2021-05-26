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
        prize = input("Please enter a prize: ")
        return prize

    def finished_entry(self):
        finished = input("Are there more contestants to enter (y/n): ")
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

    def show_info(self, first_name, last_name, email, number, sweepstake):
        print(f"The winner of {sweepstake} is contestant number {number}, name: {first_name}, {last_name},\n email: {email}\n Email with the prize information will will follow shortly.")


