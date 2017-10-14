#!/usr/bin/python3

'''This module is the base class of all the spiders '''

import ruler

class spider:
    def __init__(self , depth , spider_type):
        self.depth = depth
        # spider_type:
        # 0 - keywordspider
        # 1 - relationspider
        # 2 - websitespider
        self.spider_type = spider_type
        self.ruler = ruler.ruler()    # create the own ruler object for the spider
