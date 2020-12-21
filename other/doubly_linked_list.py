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