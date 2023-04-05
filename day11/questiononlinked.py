class Node:
    def __init__(self,data):
        self.item = data
        self.ref = None
class Linkedlist:
    def __init__(self):
        self.start_node = None
        
    

    def insert_at_end(self,data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n = n.ref
        n.ref = new_node
     
    
    def replace_list(self,x):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            res = -1
            while n is not None:
                res = max(res,n.item)
                n = n.ref       
            n = self.start_node
            while n is not None:
                if n.item == res:
                    n.item = x
                n.ref

    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item," ")
                n = n.ref 
ll1  = Linkedlist()
ll1.insert_at_end(1)
ll1.insert_at_end(2)
ll1.insert_at_end(7)
ll1.insert_at_end(3)
ll1.insert_at_end(5)
print("before replacing")
ll1.traverse_list()
print("\nafter replacing")
ll1.replace_list(6)
ll1.traverse_list()

