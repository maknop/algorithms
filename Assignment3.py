class Node:
    def __init__(self, data):
        self.Data = data
        self.nextnode = None

    def setdata(self, data):
        self.Data = data

    def getdata(self):
        return self.Data

    def setnextnode(self, node):
        self.nextnode = node

class Linked_List:
    def __init__(self):
        self.head = None

    def Add(self,item):
         new = Node(item)
         new.nextnode = self.head
         self.head = new
         # O(1)

    def remove(self, key):
        temp = self.head
        if (temp is not None):
            if (temp.Data == key):
                self.head = temp.nextnode
                temp = None
                return
        while(temp is not None):
            if temp.Data == key:
                break
            prev = temp
            temp = temp.nextnode
        if(temp == None):
            print("error - item not in list")
            return
        prev.nextnode = temp.nextnode
        temp = None
        # O(n)

    def search(self,key):
        temp = self.head
        while(temp is not None):
            if(temp.Data == key):
                return True
            prev = temp
            temp = temp.nextnode
        return False
        # O(n)

    def isEmpty(self):
        if(self.head == None):
            return True
        return False
        # O(1)

    def size(self):
        temp = self.head
        count=0
        while(temp is not None):
            count+=1
            prev = temp
            temp = temp.nextnode
        return count
        # O(1)

    def append(self, item):
        new = Node(item)
        if self.head is None:
            self.head = new
            return
        last = self.head
        while (last.nextnode):
            last = last.nextnode
        last.nextnode =  new

    def getIndex(self,data):
        index=0
        there = False
        temp=self.head
        if(temp.Data==data):
            there= True
            return index
        index+=1
        while(temp.nextnode):
            temp=temp.nextnode
            if(temp.Data==data):
                there= True
                return index
            index+=1
        if(there== False):
            return "Item not found"

    def insert(self,item,position):
        temp2 = self.head
        count=0
        while(temp2 is not None):
            count+=1
            prev = temp2
            temp2 = temp2.nextnode
        if(position>count):
            print("Index out of bounds")
        elif(position==0):
            new = Node(item)
            new.nextnode = self.head
            self.head = new
        else:
            temp=self.head
            count=0
            while(temp is not None):
                if(count==position-1):
                    break
                else:
                    count+=1
                    temp=temp.nextnode
            new=Node(item)
            new.nextnode=temp.nextnode
            temp.nextnode=new
            # O(n)

    def pop(self):
        temp2 = self.head
        count=0
        while(temp2 is not None):
            count+=1
            prev = temp2
            temp2 = temp2.nextnode
        if(count==0):
            return "Empty list"
        if(count==1):
            RT=self.head.Data
            self.head=None
            return RT
        temp=self.head
        count=0;
        while (temp.nextnode):
            prev = temp
            temp = temp.nextnode
        RT = prev.nextnode
        prev.nextnode = None
        return RT.Data

    def pop(self,pos):
        temp2 = self.head
        count=0
        while(temp2 is not None):
            count+=1
            prev = temp2
            temp2 = temp2.nextnode
        if(count==0):
            return "Empty list"
        if(pos>=count):
            return "Out of bounds"
        temp = self.head
        if(pos==0):
           prev = temp
           temp = temp.nextnode
           RT = prev
           self.head= temp
           prev = None
           return RT.Data
        temp=self.head
        count=0
        while(temp is not None):
            if(count==pos):
                break
            else:
              count+=1
              prev = temp
              temp=temp.nextnode
        RT=temp.Data
        prev.nextnode = temp.nextnode
        temp = None
        return RT


    def printList(self):
        temp = self.head
        while (temp):
            print(temp.Data)
            temp = temp.nextnode

## double linked lists
class Node:
    def __init__(self, data):
        self.Data = data
        self.nextnode = None
        self.prevnode = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def Add(self,item):
        if(self.head is None):
            new = Node(item)
            self.head = new
            return
        new = Node(item)
        new.nextnode = self.head
        self.head.prevnode = new
        self.head = new

    def remove(self,item):
        if(self.head is None):
           return "List is empty"
        if(self.head.nextnode is None):
            if(self.head.Data == item):
               self.head = None
               return
            else:
               return "Item not found"
        if(self.head.Data == item):
            self.head = self.head.nextnode
            self.head.prevnode = None
            return
        temp = self.head
        while(temp.nextnode is not None):
            if(temp.Data == item):
                break
            temp = temp.nextnode
        if(temp.nextnode is not None):
            temp.prevnode.nextnode = temp.nextnode
            temp.nextnode.prevnode = temp.prevnode
        else:
            if(temp.Data == item):
                temp.prevnode.nextnode = None
                return
            else:
                return "Item not found"

    def search(self,key):
        temp = self.head
        while(temp is not None):
            if(temp.Data == key):
                return True
            prev = temp
            temp = temp.nextnode
        return False

    def isEmpty(self):
        if(self.head == None):
            return True
        return False

    def size(self):
        temp = self.head
        count=0
        while(temp is not None):
            count+=1
            prev = temp
            temp = temp.nextnode
        return count

    def append(self,item):
        if(self.head is None):
            new = Node(item)
            self.head = new
            return
        temp = self.head
        while(temp.nextnode is not None):
            temp = temp.nextnode
        new = Node(item)
        temp.nextnode = new
        new.prevnode = temp

    def getIndex(self,data):
        index=0
        there = False
        temp=self.head
        if(temp.Data==data):
            there= True
            return index
        index+=1
        while(temp.nextnode):
            temp=temp.nextnode
            if(temp.Data==data):
                there= True
                return index
            index+=1
        if(there== False):
            return "Item not found"

    def insert(self,item,position):
        temp2=self.head
        count = 0
        while(temp2 is not None):
            count += 1
            prev = temp2
            temp2 = temp2.nextnode
        if(position>count):
            print("Index out of bounds")
        elif(position==0):
            if(count==0):
                new = Node(item)
                self.head = new
            if(count>1):
                new = Node(item)
                new.nextnode = self.head
                self.head.prevnode = new
                self.head = new
        else:
            temp = self.head
            count = 0
            while(temp is not None):
                if(count==position-1):
                    break
                else:
                    count+=1
                    temp = temp.nextnode
            new=Node(item)
            new.nextnode = temp.nextnode
            temp.nextnode = new
            new.prevnode = temp
            new.nextnode.prevnode = new

    def pop(self):
        if(self.head is None):
            return "Empty list"
        if(self.head.nextnode is None):
            RT = self.head.Data
            self.head = None
            return RT
        temp = self.head
        while(temp.nextnode is not None):
            temp = temp.nextnode
        RT=temp.prevnode.nextnode.Data
        temp.prevnode.nextnode = None
        return RT

    def pop(self,pos):
        temp2 = self.head
        count=0
        while(temp2 is not None):
            count+=1
            prev = temp2
            temp2 = temp2.nextnode
        if(count==0):
            return "Empty list"
        if(pos>=count):
            return "Out of bounds"
        temp = self.head
        if(pos==0):
           self.head = temp.nextnode
           RT = temp.Data
           temp = None
           return RT
        if(pos==count-1):
           temp=self.head
           count=0
           while(temp is not None):
               if(count==pos):
                   break
               else:
                   count+=1
                   prev = temp
                   temp=temp.nextnode
           RT=temp.prevnode.nextnode.Data
           temp.prevnode.nextnode = None
           return RT
        temp=self.head
        count=0
        while(temp is not None):
            if(count==pos):
                break
            else:
              count+=1
              prev = temp
              temp=temp.nextnode
        RT=temp.Data
        temp.nextnode.prevnode = temp.prevnode
        temp.prevnode.nextnode = temp.nextnode
        temp = None
        return RT

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.Data)
            temp = temp.nextnode


# Question 3
# -----------
# Linked Lists:
#       O(1) -->  add(), isEmpty()
#
#       O(n) -->  remove(), search(), size(), append(), getindex(), insert(),
#                 pop(), pop(i)
#
# Doubly Linked Lists:
#       O(1) -->  add(), isEmpty()
#
#       O(n) -->  remove(), search(), size(), append(), getindex(), insert(),
#                 pop(), pop(i)
#
# Lists:
#       O(1) --> pop(), len(), append()
#
#       O(n) --> pop(i), insert(), del(), index()
#
# When comparing the running times between python's list methods and the running
# of the linked-list and doubly-linked list methods, we found that there seems to not be
# a clear correlation between them. So we believe that the internal representation
# of a python's list is not a linked-list nor a doubly-linked-list



## stack
class Stack:
    def __init__(self):
        self.stack=[]

    def push(self,item):
        self.stack.append(item)
        # this runs in O(1) time

    def pop(self):
        return self.stack.pop()
        # this runs in O(1) time

    def peek(self):
        temp = len(self.stack) -1
        return self.stack[temp]
        # this runs in O(1) time

    def isEmpty(self):
        if(len(self.stack)==0):
            return True
        else:
            return False
        # this runs in O(1) time

    def size(self):
        return len(self.stack)
        # this runs in O(1) time


## Queues
class Queues:
    def __init__(self):
        self.queues = []

    def enqueue(self, item):
        self.queues.append(item)
        # this runs in O(1) time

    def dequeue(self):
        return self.queues.pop(0)
        # this runs in O(n) time

    def isEmpty(self):
        if(len(self.queues)==0):
            return True
        else:
            return False
        # this runs in O(1) time

    def size(self):
        return len(self.queues)
        # this runs in O(1) time

## Deque
class Deque:
    def __init__(self):
        self.deque = []

    def addFront(self, item):
        self.deque.insert(0, item)
        # this runs in O(n) time

    def addRear(self, item):
        self.deque.append(item)
        # this runs in O(1) time

    def removeFront(self):
        return self.deque.pop(0)
        # this runs in O(n) time

    def removeRear(self):
        return self.deque.pop()
        # this runs in O(1) time

    def isEmpty(self):
        if(len(self.deque)==0):
            return True
        else:
            return False
        # this runs in O(1) time

    def printDeque(self):
        for x in self.deque:
            print(x)

    def size(self):
        return len(self.deque)
        # this runs in O(1) time