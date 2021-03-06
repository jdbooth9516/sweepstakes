from manager import Marketing_firm
import random

class Sweepstake: 

    def __init__(self, contest_name):
        self.contestants = {}
        self.name = contest_name

    def get_contestants(self,contestant):
    
        self.contestants.update({f'{contestant.registration}' : contestant})

    def get_winner(self):
        winner = random.choice(list(self.contestants.keys()))
        return winner
        

    def contestants_info(self, winner):
        

        for contestant in self.contestants:
            if contestant == winner:
                self.contestants.get(contestant).notify_winner()

            else: 
                self.contestants.get(contestant).notify()
                


        
       
