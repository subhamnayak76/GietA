class Node:
    def __init__(self,data):
        self.item = data
        self.ref = None

class Table: 
    def __init__(self):
        self.head = None

    def get_occupied_table_list(self):
        pass

    def allocate_table(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
    
    def display_table(self):
        if self.head is None:
            print("cafe is empty")
            return
        else:
            n = self.head
            while n is not None:
                print(n.item," ")
                n = n.ref
    def  deallocation(self,table_number):
        if self.head is None:
            print("the list of has no element ")
            return
        if self.head.item == table_number:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if n.ref.item == table_number:
                break
            n = n.ref

        if n.ref is None:
            print("item not found in the list")
        else:
            n.ref= n.ref.ref   

new_table = Table() 
new_table.allocate_table(1)
new_table.allocate_table(2)
new_table.allocate_table(3)
new_table.allocate_table(4)
new_table.display_table()  
new_table.deallocation(2)
new_table.display_table()