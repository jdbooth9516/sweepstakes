from user_interface import User_interface
from queue_manager import *
from stack_manager import * 


class Marketing_firm:
    def __init__(self,manager_type):
        self.ui = User_interface()
        self.manager_type = manager_type
        
    def add_sweepstake(self):
        sweepstake = self.ui.get_sweepstakes_info()
        #using depenancy injection to send sweepstake info to either data managers
        self.manager_type.insert_sweepstake(sweepstake)
