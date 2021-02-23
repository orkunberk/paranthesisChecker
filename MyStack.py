# -*- coding: utf-8 -*-

class MyStack:
    """ Stack implementation using lists """

    def __init__(self):
        """ create an empty stack """
        self.data = []

    def get_size(self):
        return(len(self.data))

    def is_empty(self):
        return(len(self.data)==0)

    def push(self, e):
        self.data.append(e)

    def top(self):
        if(len(self.data)>0):
            return(self.data[-1])

    def pop(self):
        if(len(self.data)>0):
            return(self.data.pop())
        else:
            return('<<<stack is empty>. cannot pop an element>>')

    def print_stack(self):
        if(len(self.data)>0):
            return(''.join(str(x) for x in self.data))
        else:
            return('<<< empty stack >>>')