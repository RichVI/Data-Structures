from singly_linked_list import LinkedList
"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Stack:
    def __init__(self):
        self.size = 0

        # Array Structure
        self.storage = []

    def __len__(self):
        # Returns the length of array
        return self.size

    def push(self, value):
        # Increase the array size by 1
        self.size += 1
        # Add the new value to the top of the stack
        self.storage.append(value)


    def pop(self):
        # If array size is 0, then return None
        if self.size == 0:
            return None
        
        # Else 
        # 1) Decrease the size of the array by 1
        # 2) Remove the item on the top of the stack
        else:
            self.size -= 1
            return self.storage.pop()

# class Stack:
#     def __init__(self):
#         self.size = 0

#         # Array Structure
#         self.storage = LinkedList()

#     def __len__(self):
#         # Returns the length of array
#         return self.size

#     def push(self, value):
#         # Increase the array size by 1
#         self.size += 1
#         # Add the new value to the tail of the linkedlist
#         self.storage.add_to_tail(value)


#     def pop(self):
#         # If array size is 0, then return None
#         if self.size == 0:
#             return None
        
#         # Else 
#         # 1) Decrease the size of the array by 1
#         # 2) Remove the tail from the linkedlist
#         else:
#             self.size -= 1
#             return self.storage.remove_tail()