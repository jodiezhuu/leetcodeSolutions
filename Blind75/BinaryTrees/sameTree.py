# Given the roots of two binary trees `p` and `q`, write a function to check 
# if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, 
# and the nodes have the same value.

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif (p is None and q) or (p and q is None):
            return False
        else:
            left = self.isSameTree(p.left, q.left)
            right = self.isSameTree(p.right, q.right)
            return (p.val == q.val) and left and right