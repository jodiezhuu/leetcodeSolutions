# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made 
# by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.
# Time Complexity: O(n)
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() ## by default, first node is 0
        curr = dummy ## pointer to first element of dummy
        while (list1 is not None) and (list2 is not None):
            if (list1.val <= list2.val):
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        if list1:
            curr.next = list1
        else:
            curr.next = list2
        return dummy.next ## since first node of dummy is 0