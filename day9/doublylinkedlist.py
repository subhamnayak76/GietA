class Node:
    def __init__(self,value):
        self.prev = None
        self.data = value
        self.next = None


class DoublylinkedList:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        if self.head is None:
            return True
        return False
    def length(self):
        temp = self.head
        count = 0
        while temp is not None:
            temp = temp.next
            count += 1
        return count

    def insertAtBeginning(self,value):
        new_node = Node(value)
        if self.isEmpty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    def insertAtPostion(self,value,postion):
        temp = self.head
        count = 1
        while temp is not None:
            if count == postion - 1:
                break
            count += 1
            temp = temp.next
        if postion == 1:
            self.insertAtBeginning(value)
        elif temp is None:
            print("there are less than {}-1 elements in the linked list")
        elif temp.next is None:
            self.insertAtend(value)

        else:
            new_node = Node(value)
            new_node.next = temp.next
            new_node.prev = temp
            temp.next.prev = new_node   
            temp.next = new_node                    
    def insertAtend(self,value):
        new_node = Node(value)
        if self.isEmpty():
            self.insertAtBeginning(value)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
    def deleteFromlast(self):
        if self.isEmpty():
            print("linked list is empty.cannot delete elements")
        elif self.head.next is None:
            self.head = None
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.prev.next = None
            temp.prev = None               
    def deleteFromBeginning(self):
        if self.isEmpty():
            print("Linked List is empty. Cannot delete")
        elif self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None
    def deleteFromPosition(self,position):
        if self.isEmpty():
            print("linked list is empty . cannot delete elements")
        elif position == 1:
            self.deleteFromBeginning()
        else:
            temp = self.head
            count = 1
            while temp is not None:
                if count == position:
                    break
                temp = temp.next
                count = count + 1

            if temp is None:
                
                print("there are less than {} elements in linked list .cannot delete element".format(position))
                return
            elif temp.next is None:
                self.deleteFromLast()
                return
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            temp.next = None
            temp.prev = None                              
    def printLinkedList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

x = DoublylinkedList()
print(x.isEmpty())
x.insertAtBeginning(5)
x.printLinkedList()
x.insertAtBeginning(15)
x.insertAtBeginning(25)
x.insertAtBeginning(35)
x.insertAtend(60)
x.insertAtend(76)
x.insertAtend(67)
x.printLinkedList()
print("no of nodes",x.length())
print("insert at position of 2 number 8")
x.insertAtPostion(8,2)
x.deleteFromBeginning()
print("delete from beginning")
x.printLinkedList()
print("delete at the last")
x.deleteFromlast()
x.printLinkedList()

x.deleteFromPosition(2)
print("delete the element")
x.printLinkedList()

