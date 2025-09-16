class Node:
    def __init__(self,initval=None):
        self.value=initval
        self.next=None
    def isempty(self):
        return(self.value==None)