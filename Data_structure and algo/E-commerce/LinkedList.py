class Node:
    def __init__(self, data=None, next=None):
        self.data = data # # The data stored in this node is an instance variable (or attribute) that belongs to that specific object.
        self.next = next  #pointer for next node
class LinkedList:
    def __init__(self, head=None):
        self.head = head
    def print(self):
        if self.head is None:
            print("Linked List is empty.")
        itr = self.head
        li = ''
        while itr:
            li += str(itr.data) + '->' if itr.next else str(itr.data)
            itr = itr.next
        print(li)
    def getlen(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    def insert_at_beginning(self,val):
        node = Node(val, self.head)
        self.head = node

    def insert_at_end(self, val):
        if self.head is None:
            self.head = Node(val,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(val,None)
    def insert_at(self, index, data):
        if index < 0 or index > self.getlen():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_beginning(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1
    def remove_at(self,index):
        if index<0 or index>self.getlen():
            raise Exception("Invalid")
        if index == 0:
            self.head = self.head.next
            return
        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
    def insertval(self,lis):
        self.head = None
        for data in lis:
            self.insert_at_end(data)
    def insert_after_value(self,li1,li2):
        itr = self.head
        while itr:
            if itr.data == li1:
                node = Node(li2,itr.next)
                itr.next = node
                break
            itr = itr.next
    def remove_by_value(self,li):
        if self.head is None:
            print("Empty")
            return
        if self.head.data == li:
            self.head = self.head.next
            return
        itr = self.head
        while itr.next:
            if itr.next.data == li:
                itr.next = itr.next.next
                return
            itr = itr.next
        print("Not in list")

if __name__ == '__main__':
    ll = LinkedList()
    ll.insertval(["banana", "mango", "grapes", "orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()






