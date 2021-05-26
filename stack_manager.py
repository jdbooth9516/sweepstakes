from stack import Stack 

class Stack_manager:
    def __init__(self):
        self.stack = Stack()

    def insert_sweepstake(self, sweepstake):
        self.stack.push(sweepstake)

    def get_sweepstake(self):
        return self.stack.pop()
        
    #create insert sweepstakes and get sweepstakes method.

    