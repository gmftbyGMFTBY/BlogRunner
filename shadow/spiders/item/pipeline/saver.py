#!/usr/bin/python3

'''该模块定义saver对象的基本类型和属性，之后可以在之上扩展saver插件，子类继承实现'''

class saver:
    def __init__(self , signal):
        self.signal = signal     # signal是信号，用来制定数据流在pipeline中的传输状态


