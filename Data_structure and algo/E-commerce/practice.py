class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
class LinkedIn:
    def __init__(self, head=None):
        self.head = head
    def print(self):
        if self.head is None:
            print("Empty Linked List.")
            return
        itr = self.head
        li = ''
        while itr:
            li += str(itr.data) + '->' if itr.next else str(itr.data)
            itr = itr.next
        print(li)
    def get_length(self):
        if self.head is None:
            return 0
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    def insert_beginning(self,val):
        node = Node(val, self.head)
        self.head = node
    def insert_at_end(self,val):
        if self.head is None:
            self.head = Node(val,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(val,None)
    def insert_at_index(self,index, val):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index.")
        if index == 0:
            self.insert_beginning(val)
        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                node = Node(val, itr.next)
                itr.next = node
                break
            count += 1
            itr = itr.next
    def remove_at_index(self,index):
        if index < 0 or index>self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
            return
        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                if itr.next:
                    itr.next = itr.next.next
                break
            count += 1
            itr = itr.next
    def insert_by_values(self,target,val):
        itr = self.head
        while itr:
            if itr.data == target:
                itr.next = Node(val, itr.next)
                break
            itr = itr.next

    def remove_by_values(self, val):
        if self.head is None:
            return
        if self.head.data == val:
            self.head = self.head.next
        itr = self.head
        while itr.next:
            if itr.next.data == val:
                itr.next = itr.next.next
                return
            itr = itr.next
    def insert_values(self, val):
        self.head = None
        for da in val:
            self.insert_at_end(da)
if __name__ == '__main__':
    li = LinkedIn()
    li.insert_values([10, 20, 30, 40])
    li.print()
    li.insert_beginning(25)
    li.print()
    li.insert_at_end(50)
    li.print()
    li.insert_at_index(2,35)
    li.print()
    li.insert_by_values(20,22)
    li.print()
    li.remove_at_index(0)
    li.print()
    li.remove_by_values(22)
    li.print()
    #li.insert_values()









