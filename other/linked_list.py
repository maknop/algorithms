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