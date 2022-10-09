# Given the rootof a binary tree, invert the tree, and return its root.

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case 
        if root is None:
            return root
        else:
            temp = root.left
            root.left = self.invertTree(root.right)
            root.right = self.invertTree(temp)
            return root