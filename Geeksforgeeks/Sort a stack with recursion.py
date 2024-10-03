class Solution:
    # Function to sort the stack using recursion
    def Sorted(self, s):
        # Base case: If stack is empty, return
        if not s:
            return

        # Remove the top element and sort the remaining stack
        temp = s.pop()
        self.Sorted(s)

        self.insert_in_sorted_stack(s, temp)

    # Helper function
    def insert_in_sorted_stack(self, s, element):

        if not s or s[-1] <= element:
            s.append(element)
            return

        # If top of the stack is greater, pop the top element and recurse
        temp = s.pop()
        self.insert_in_sorted_stack(s, element)

        # Push the popped element back after inserting 'element'
        s.append(temp)