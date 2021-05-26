from stack import Stack
from stack_manager import Stack_manager
from manager import *
from user_interface import User_interface
from stack_manager import Stack_manager

class Run_simulation:

    def __init__(self):
        self.ui = User_interface()
        self.choice = None
        self.firm = None
        self.stack = Stack_manager()

    def choose_manager_type(self):
        manager_type = self.ui.get_manager_type()
        self.choice = manager_type

    def run(self):
        self.choose_manager_type()
        if self.choice == 'stack':
            manager = Marketing_firm(self.stack)
        elif self.choice == 'queue':
            manager = Marketing_firm(self.choice)
        manager.add_sweepstake()




