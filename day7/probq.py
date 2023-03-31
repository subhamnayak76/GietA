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

    def display_result(self):
        for index in range(self.__front,self.__rear+1):
           if (self.itreate(self.__elements[index]))== True:
               print(self.__elements[index])
    def itreate(self,data):
        for i in range(1,10+1):
            if data % i != 0:
                return False
                break
        return True

    def get_max_size(self):
        return self.__max_size

queue2 = Queue(5)
queue2.enqueue(13983)
queue2.enqueue(10080)
queue2.enqueue(7113)
queue2.enqueue(2520)
queue2.enqueue(2500)
queue2.display_result()
