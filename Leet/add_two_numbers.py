# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        result = str(self.listing(l1) + self.listing(l2))
        reversed_digits = result[::-1]
        head = None
        current = None

        for digit_char in reversed_digits:
            digit = int(digit_char)
            new_node = ListNode(digit)

            if head is None:
                head = new_node       
                current = new_node
            else:
                current.next = new_node  
                current = new_node

        return head
        
    def listing(self, listing: ListNode):
        current = listing
        values = []
        while current is not None:
            values.append(current.val)
            current = current.next
        
        values_reversed = values[::-1]
        digit_string = "".join(map(str, values_reversed))
        return int(digit_string)

        