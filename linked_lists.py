# Definition for singly-linked list.
class ListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    #insertion method for the class
    
    def append(self, data):

        new_node = Node(data)

        if not self.head:
            self.head = new_node    #if there is no head, new node is it
        
        if self.tail:
            self.tail.next = new_node   #append to end

"""
Given a Linke List class create a method to determine if the linked list is a palindrome
"""

    def isPalindrome(self, head):
        lst = []                    #make an empty list
        current = head              #create a current variable
        while current:
            lst.append(current.val) #add values to list
            current = current.next  #traverse through llist
        return lst == lst[::-1]     #if the list equals the list in reverse, it is True.
    
    #Answer has runtime of O(n) and space of O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

    def addTwoNumbers(self, l1, l2)
        return_head = ListNode(0)           # current = head of returned list
        current = return_head
        carry = 0                           # carry set to 0
        while l1 or l2 or carry:            # loop until ends of list and carry is 0
            l1_data = l1.data if l1 else 0    # variables set to the value unless at end
            l2_data = l2.data if l2 else 0
            column_sum = l1_data + l2_data + carry    # add column and carry 
            carry = column_sum // 10                # update carry to column sum/10 and rounded
            new_Node = ListNode(column_sum % 10)    # create new node with value of sum MOD 10
            current.next = new_Node                 # assign it to current.next
            current = new_Node                      # assign to it to current
            l1 = l1.next if l1 else None            # advance to the next 
            l2 = l2.next if l2 else None
        return return_head.next                 
