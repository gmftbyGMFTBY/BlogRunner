#!/usr/bin/python3

'''this module define the scheduler object for the module'''

from queue import Queue

class scheduler:
    def __init__(self):
        '''
        begin , there is nothing in the scheduler
        '''
        self.photo_queue = Queue()    # create the multiprocessing queue for the scheuler
        self.html_queue = Queue()
        self.memory = []

