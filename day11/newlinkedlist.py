class Node:
    def __init__(self,data):
        self.item = data
        self.ref = None
class Linkedlist:
    def __init__(self):
        self.start_node = None

    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item," ")
                n = n.ref

    def insert_at_end(self,data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n = n.ref
        n.ref = new_node
    def insert_at_index(self,index,data):
        if index == 1:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
        i = 1
        n = self.start_node
        while i < index - 1 and n is not None:
            n = n.ref
            i = i + 1
        if n is None:
            print("index out of bound")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node       

    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                res = max(res,n.item)
                n = n.ref       

ll1  = Linkedlist()
ll1.insert_at_end(1)
ll1.insert_at_end(2)
ll1.insert_at_end(4)
ll1.insert_at_end(3)
ll1.insert_at_end(5)
ll2 = Linkedlist()
n = int(input())
ll1.insert_at_index(3,9)
ll1.insert_at_index(4,8)
ll1.insert_at_index(5,11)
ll1.traverse_list()


