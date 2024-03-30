# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        s = []
        def dfs(node, s, low, high):
            if node is not None:
                dfs(node.left, s, low, high)
                dfs(node.right, s, low, high)
                if node.val >= low and node.val <= high:
                    s.append(node.val)
            return s
        
        return sum(dfs(root, s, low, high))
