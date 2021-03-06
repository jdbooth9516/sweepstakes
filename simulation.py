from sweepstake import Sweepstake
from stack_manager import Stack_manager
from manager import *
from user_interface import User_interface
from stack_manager import Stack_manager
from contestant import Contestant

class Run_simulation:

    def __init__(self):
        self.ui = User_interface()
        self.choice = None
        self.firm = None
        self.loop = False
        
  

    
    def choose_manager_type(self):
        manager_type = self.ui.get_manager_type()
        self.choice = manager_type
        # if statement to see which data structure to init

    def create_sweepstake(self):
        current_sweepstake = self.choice.get_sweepstake()
        return current_sweepstake


    def run(self):
        self.choose_manager_type()
        self.loop = True
      
            # choose which data type to use
        if self.choice == 'stack':
            self.choice = Stack_manager()
            # here the dependency is used to pass the data type and sweepstake info to the marketying firm
            manager = Marketing_firm(self.choice)
        elif self.choice == 'queue':
            # Same here for dependency
            self.choice = Queue_manager()
            manager = Marketing_firm(self.choice)


        #MAIN LOOP
        while self.loop:
        # Main menu routing
            user_selection = self.ui.main_menu()
            if user_selection == 1: 
                adding_sweepstakes = True
                while adding_sweepstakes:
                    manager.add_sweepstake()
                    if self.ui.finished_sweepstakes():
                        adding_sweepstakes = False 

            elif user_selection == 2:  
                active_sweepstake = self.create_sweepstake()
                sweepstake = Sweepstake(active_sweepstake)
                add_contestant = True
                while add_contestant:
                    person = self.ui.contestant_info(sweepstake.name)
                    contestant = Contestant(self.ui.first, self.ui.last, self.ui.email, self.ui.registration)
                    sweepstake.get_contestants(contestant)
                    finished = self.ui.finished_entry()  
                    if finished:
                        add_contestant = False

            elif user_selection == 3:
                self.ui.close()
                winner = sweepstake.get_winner()
                sweepstake.contestants_info(winner)

            elif user_selection == 4:
                if self.ui.finished_contest():
                    self.loop = False
            



