class Node:
    def __init__(self,data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
class LinkedList:
    def __init__(self,head=None):
        self.head = None
    def print_f(self):
        if self.head is None:
            print("Empty")
            return
        itr = self.head
        Li = ''
        while itr:
            Li += str(itr.data)+'->'
            itr = itr.next
        print(Li)
    def print_b(self):
        if self.head is None:
            print("Empty")
            return
        last_node = self.get_last_node()
        itr = last_node
        li = ''
        while itr:
            li += str(itr) + '->'
            itr = itr.prev
        print("Reverse Linked List: ", li)
    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr
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
        if self.head is None:
            self.head = Node(val,None,None)
        else:
            node = Node(val,self.head,None)
            self.head.prev = node
            self.head = node
    def insert_at_end(self,val):
        if self.head is None:
            node = Node(val,None,None)
            self.head = node
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(val,None, itr)
    def insert_at_index(self,index,val):
        if index<0 or index>self.get_length():
            raise Exception("Invalid")
        if index == 0:
            self.insert_at_beginning(val)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(val,itr.next,itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                itr.next.prev = node
                break
            count += 1
            itr = itr.next
    def remove_at_index(self,index):
        if index < 0 or index>self.get_length():
            raise Expception("Invalid")
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break
            itr = itr.next
            count += 1
    def insert_values(self,li):
        self.head = None
        for data in li:
            self.insert_at_end(data)
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print_f()
    ll.print_b()
    ll.insert_at_end("figs")
    ll.print_f()
    ll.insert_at_index(0, "jackfruit")
    ll.print_f()
    ll.insert_at_index(6, "dates")
    ll.print_f()
    ll.insert_at_index(2, "kiwi")
    ll.print_f()
    ll.remove_at_index(6)
    ll.print_f()








