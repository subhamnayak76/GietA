class Node:
    def __init__(self,dataval = None):
        self.dataval = dataval
        self.nextval = None

class SlinkedList:
    def __init__(self):
        self.headval = None                
    def Atbegin(self,newdata):
        NewNode = Node(newdata)
        NewNode.headval = self.headval
        self.headval = NewNode     
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
    def Atbegin(self,newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode        
l = SlinkedList()
l.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
l.headval.nextval = e2
e2.nextval = e3
l.Atbegin("Sun")
l.listprint()                
