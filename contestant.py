from user_interface import User_interface

class Contestant:
    def __init__(self, fname, lname, email, registration_number):
        self.first_name = fname
        self.last_name = lname
        self.email = email
        self.registration = registration_number
        self.ui = User_interface()
       

    def notify(self):
        self.ui.recieved_message(self.first_name)

    def notify_winner (self):
        self.ui.recieve_winner(self.first_name)