# Given the `head` of a linked list, remove the `nth`node 
# from the end of the list and return its head.
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next 
        if length == 1 and n == 1:
            return None
        # curr points at end of linked list 
        prev = length - n
        # edge case: if first node is removed
        if prev == 0:
            head = head.next
            return head
        curr = head # point back to head 
        # only works if node is not first node
        while (prev > 1):
            curr = curr.next
            prev -= 1 
        temp = curr.next # removed node
        curr.next = temp.next # next node from removed 
        return head