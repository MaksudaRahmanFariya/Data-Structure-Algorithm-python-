from collections import deque
import threading
import time

class solution:
    def __init__(self):
        self.buffer = deque()
    def enqueue(self, val):
        self.buffer.appendleft(val)
    def deque(self):
        if len(self.buffer) == 0:
            print("Queue is empty")
            return
        return self.buffer.pop()
    def is_empty(self):
        return len(self.buffer) == 0
    def size(self):
        return len(self.buffer)
food_order = solution()
def place_order(orders):
    for order in orders:
        print("Placing order for:", order)
        food_order.enqueue(order)
        time.sleep(0.5)
def serve():
    time.sleep(1)
    while True:
        order = food_order.deque()
        print("Now serving: ", order)
        time.sleep(2)
if __name__ == '__main__':
    orders = ['pizza','samosa','pasta','biryani','burger']
    t1 = threading.Thread(target=place_order, args=(orders,))
    t2 = threading.Thread(target=serve)

    t1.start()
    t2.start()



