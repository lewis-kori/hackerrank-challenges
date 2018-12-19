class Queue:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items==[]
    def enqueue(self,item):
        self.items.insert(0,item)
    def deqeue(self):
        return self.items.pop()
    def print_queue(self):
        print(self.items)

q= Queue()
q.enqueue('a')
q.enqueue('b')
q.enqueue('78')
q.print_queue()

q.deqeue()
q.print_queue()
