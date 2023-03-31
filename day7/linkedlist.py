# travising a linked list
class Node:
    def __init__(self,dataval = None):
        self.dataval = dataval
        self.nextval = None

class SlinkedList:
    def __init__(self):
        self.headval = None                
        
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
l = SlinkedList()
l.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
l.headval.nextval = e2
e2.nextval = e3
l.listprint()                

