#!/usr/bin/python3

'''This module define the ruler for the spider to crawl the website , this module is for HTML_item object not for photo_item'''
class ruler:
    def __init__(self):
        '''
        init the dict and define some API for it
        '''
        self.rule = {}   # empty ruler contain
        # init for the rule
        self.add_rule('content' , None)
        self.add_rule('img' , None)    # the img if extracted from the content
        self.add_rule('next' , None)
        self.add_rule('number_visitor' , None)
        self.add_rule('number_issue' , None)
        self.add_rule('issue' , None)
        print(self.rule)
    def add_rule(self , key , value):
        self.rule.setdefault(key , value)
        return True
    def change_rule(self , key , value):
        try:
            self.rule[key] = value
            return True
        except KeyError:
            print("The rule you point does not exist!")
            return False
