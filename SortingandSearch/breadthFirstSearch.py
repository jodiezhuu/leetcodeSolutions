def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        res = []
        queue = deque()
        queue.append(root)
        while (queue):
            level = []
            for i in range(len(queue)): ## prints all the node vals in the level
                node = queue.popleft()
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    level.append(node.val)
            if len(level) > 0:
                res.append(level)
        return res

