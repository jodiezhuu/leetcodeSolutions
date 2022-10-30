class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while (fast and fast.next): # slow should be in the middle of linked list
            tmp = slow
            slow = slow.next
            fast = fast.next.next
        # reverse last half linked list
        prev = None
        while (slow):
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        left = head
        right = prev
        # check palindrome
        while (right):
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True