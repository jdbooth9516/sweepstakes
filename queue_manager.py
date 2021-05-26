from queue import Queue

class Queue_manager:
    def __init__(self):
        self.queue = Queue()

    def insert_sweepstake(self, sweepstake):
        self.queue.enqueue(sweepstake)

    def get_sweepstake(self):
        return self.queue.dequeue()

        
        

    #create insert sweepstakes and get sweepstakes method.