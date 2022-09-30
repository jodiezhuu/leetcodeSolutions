# Time Complexity: O(3*n) = O(n)

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        ## split into two sub linked lists using tortoise and hare method
        slow = head
        fast = head.next
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        ## reverse right linked list 
        curr_right_node = slow.next
        prev = None ## points at reversed linked list
        while (curr_right_node):
            ptr = curr_right_node
            temp = curr_right_node.next
            curr_right_node.next = prev
            prev = curr_right_node
            curr_right_node = temp
        ## alternately point at each node of the linked list 
        index = head
        slow.next = None
        right_node = prev
        while (right_node is not None and index is not None):
            temp_left = index.next
            temp_right = right_node.next
            index.next = right_node
            right_node.next = temp_left
            index = temp_left
            right_node = temp_right