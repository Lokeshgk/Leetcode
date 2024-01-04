# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        frequency = {}
        def dfs(node, frequency):
            if node is not None:
                if node.val in frequency:
                    frequency[node.val] += 1
                else:
                    frequency[node.val] = 1
                dfs(node.left, frequency)
                dfs(node.right, frequency)
            return frequency
        freq = dfs(root, frequency)
        res = [key for key, value in frequency.items() if value == max(frequency.values())]
        return res
