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
    def Atbegin(self,newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode             
    def Atend(self,newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return        
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval = NewNode  

        
    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("the mentioned node is absent ")
            return
        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode      


l = SlinkedList()
l.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
l.headval.nextval = e2
e2.nextval = e3
l.Atbegin("Sun")
l.Inbetween(e3,"Fri")

l.Atend("Thu")
l.listprint()          