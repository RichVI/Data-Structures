from sll_queue import Queue
from sll_stack import Stack
"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # If new node is less than root
        if value < self.value:
            # If there is no left node
            if self.left is None:
                # Assign new_node to left node
                self.left = BSTNode(value)
            else:
                # Recursion
                return self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                return self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # If there is only one node(root)
        if target == self.value:
            return True
        if target > self.value:
            # If there is a right, then use recursion
            if self.right:
                return self.right.contains(target)
            # Else, target node does not exist
            else:
                False
        if target < self.value:
            if self.left:
                return self.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn) 

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left is not None:
            self.in_order_print(node.left)
        print(node.value)
        if node.right is not None:
            self.in_order_print(node.right)
        return

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()                 
        queue.enqueue(node)             
        while queue.__len__() > 0:                
            popped = queue.dequeue()                              
            print(popped.value)   
            if popped.left:                          
                queue.enqueue(popped.left)
            if popped.right:                                       
                queue.enqueue(popped.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()                                           
        stack.push(node)                              
        while stack.__len__() > 0:                               
            popped = stack.pop()                              
            print(popped.value)                  
            if popped.left:                                       
                stack.push(popped.left)
            if popped.right:                                        
                stack.push(popped.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
