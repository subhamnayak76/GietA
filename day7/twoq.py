class Queue:
    def __init__(self,max_size):
        self.__max_size = max_size
        self.__elements =[None]*self.__max_size
        self.__rear = -1
        self.__front = 0

    def is_full(self):
        if(self.__rear == self.__max_size - 1):
            return True
        return False

    def is_empty(self):
        if(self.__front > self.__rear):
            return True
        return False 
    
    def enqueue(self,data):
        if (self.is_full()):
            print("Queue is full")
        else:
            self.__rear += 1
            self.__elements[self.__rear] = data

    def dequeue(self):
        if (self.is_full()):
            print("Queue is full")
        else:
            data = self.__elements[self.__front]
            self.__front += 1
            return data

    def display(self):
        for index in range(self.__front,self.__rear+1):
            print(self.__elements[index])

    def get_max_size(self):
        return self.__max_size
    
    


            

queue1 = Queue(3)
queue2 = Queue(6)
queue1.enqueue(3)
queue1.enqueue(6)
queue1.enqueue(8)
queue2.enqueue('b')
queue2.enqueue('y')
queue2.enqueue('u')
queue2.enqueue('t')
queue2.enqueue('r')
queue2.enqueue('o')

size = queue1.get_max_size() + queue2.get_max_size()
def merge(queue1,queue2):
    l1 = []
    l2 = []
    l3 = []
    while (not queue1.is_empty()):
        l1.append(queue1.dequeue())
    
    while(not queue2.is_empty()):
        l2.append(queue2.dequeue())

    for i in l1:
        

        

        



