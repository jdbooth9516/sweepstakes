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
        length = len(self.contestants) - 1 
        array = []
        for i in self.contestants:
            array.append(i)

        random_number = random.randint(0, length)
        winner = array[random_number]
        return winner
        

    def contestants_info(self, winner):
        first_name = self.contestants.get(winner).first_name
        last_name = self.contestants.get(winner).last_name
        email = self.contestants.get(winner).email
        number = self.contestants.get(winner).registration
        self.ui.show_info(first_name, last_name, email, number, self.name)

        
       
