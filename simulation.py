from sweepstake import Sweepstake
from stack_manager import Stack_manager
from manager import *
from user_interface import User_interface
from stack_manager import Stack_manager

class Run_simulation:

    def __init__(self):
        self.ui = User_interface()
        self.choice = None
        self.firm = None
  

    
    def choose_manager_type(self):
        manager_type = self.ui.get_manager_type()
        self.choice = manager_type
        # if statement to see which data structure to init

    def create_steepstake(self):
        current_sweepstake = self.choice.get_sweepstake()
        return current_sweepstake


    def run(self):
        self.choose_manager_type()

        if self.choice == 'stack':
            self.choice = Stack_manager()
            manager = Marketing_firm(self.choice)
        elif self.choice == 'queue':
            self.choice = Queue_manager()
            manager = Marketing_firm(self.choice)

        manager.add_sweepstake()

        #befor call the sweepstake get a sweepstake 
        active_sweepstake = self.create_steepstake()
        sweepstake = Sweepstake(active_sweepstake)
        
        add_contestant = True
        while add_contestant:
            person = self.ui.contestant_info()
            sweepstake.get_contestants(person)
            finished = self.ui.finished_entry() # make this function 
            if finished:
                add_contestant = False

        self.ui.close()
        winner = sweepstake.get_winner()
        winner_info = sweepstake.contestants_info()

        print(self.choice)
        print(sweepstake.name)
        print(sweepstake.contestants)
            






