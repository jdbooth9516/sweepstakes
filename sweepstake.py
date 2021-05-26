from manager import Marketing_firm
from user_interface import *
import random

class Sweepstake: 

    def __init__(self, contest_name):
        self.contestants = {}
        self.name = contest_name
        self.ui = User_interface()

    def get_contestants(self,contestant):
    
        self.contestants.update({f'{contestant.registration}' : contestant})

    def get_winner(self):
        length = len(self.contestants)
        random_number = random.randint(0, length)

        return random_number

    def contestants_info(self, winner):
        first_name = self.contestants.winner.fname
        last_name = self.contestants.winner.lname
        email = self.contestants.winner.email
        number = self.contestants.winner.number

        
       
