class Node:
    def __init__(self,data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
class LinedList:
    def __init__(self,head=None):
        self.head = head
    def print(self):
        if self.head is None:
            print("Empty")
            return
        itr = self.head
        li = ' '
        while itr:
            li += str(itr.data) + '->' if itr.next else str(itr.data)
            itr = itr.next
        print(li)
    def get_length(self):
        if self.head is None:
            return 0
        itr = self.head
        count = 0
        while itr:
            count +=1
            itr = itr.next
        return count
    def insert_at_beginning(self,val):
        node = Node(val,self.head,None)
        self.head = node
    def insert_at_end(self,val):
        if self.head is None:
            self.head = Node(val,None,None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(val,None, itr)
    def insert_at(self,index,val):
        if index<0 or index>self.get_length():
            raise Exception("Invalid")
        if index == 0:
            self.insert_at_beginning(val)
            return
        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                node = Node(val, itr.next, itr)
                itr.next = node
                break
            itr = itr.next
            count += 1
    def ins(self,li):
        self.head = None
        for data in li:
            self.insert_at_end(data)
    def remove_at(self,index):
        if index<0 or index>self.get_length():
            raise Exception("Invalid")
        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return

        itr = self.head
        count = 0
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                return
            itr = itr.next
            count += 1
    def insert_by_values(self,li1, li2):
        itr = self.head
        while itr:
            if itr.data == li1:
                node = (li2,itr.next, itr)
                if itr.next:
                    itr.next.prev = node
                itr.next = node
                return
            itr = itr.next
if __name__ == '__main__':
    ll = LinedList()
    ll.ins([10, 20, 30])
    ll.print()
    ll.insert_at(1, 15)
    ll.print()
    ll.remove_at(2)
    ll.print()
    ll.insert_by_values(10, 5)
    ll.print()

class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def print(self):
        if self.head is None:
            print("Empty")
            return
        itr = self.head
        li = ''
        while itr:
            li += str(itr.data) + ' -> ' if itr.next else str(itr.data)
            itr = itr.next
        print(li)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at_beginning(self, val):
        node = Node(val, self.head, None)
        if self.head:
            self.head.prev = node
        self.head = node

    def insert_at_end(self, val):
        if self.head is None:
            self.head = Node(val)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        new_node = Node(val, None, itr)
        itr.next = new_node

    def insert_at(self, index, val):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.insert_at_beginning(val)
            return
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                node = Node(val, itr.next, itr)
                if itr.next:
                    itr.next.prev = node
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return
        itr = self.head
        count = 0
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                return
            itr = itr.next
            count += 1

    def insert_by_values(self, target, val):
        itr = self.head
        while itr:
            if itr.data == target:
                node = Node(val, itr.next, itr)
                if itr.next:
                    itr.next.prev = node
                itr.next = node
                return
            itr = itr.next

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values([10, 20, 30])
    ll.print()
    ll.insert_at(1, 15)
    ll.print()
    ll.remove_at(2)
    ll.print()
    ll.insert_by_values(10, 5)
    ll.print()














