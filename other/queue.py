class Queues:
    def __init__(self):
        self.queues = []

    def enqueue(self, item):
        self.queues.append(item)

    def dequeue(self):
        return self.queues.pop(0)

    def isEmpty(self):
        if(len(self.queues)==0):
            return True
        else:
            return False

    def size(self):
        return len(self.queues)