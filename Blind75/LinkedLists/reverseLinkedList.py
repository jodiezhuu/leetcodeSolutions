# Given the head of a singly linked list, reverse the list, and return the reversed list.
# Time Complexity: O(n)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = previous
            previous = curr
            curr = next_node
        return previous