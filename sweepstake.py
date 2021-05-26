from manager import Marketing_firm
from user_interface import *

class Sweepstake: 

    def __init__(self, contest_name):
        self.contestants = {}
        self.name = contest_name
        self.ui = User_interface()

    def get_contestants(self,contestant):
        self.contestants.update({f'{contestant.registration}' : contestant})

        
       
