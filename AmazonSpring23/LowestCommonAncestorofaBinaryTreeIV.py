# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':

        def dfs(current_node, node_vals):
            # print(current_node, "\n")
            if current_node is None or current_node in node_vals:
                return current_node
            left, right = dfs(current_node.left, node_vals), dfs(current_node.right, node_vals)
            if left and right:
                return current_node
            return left or right
        
        return dfs(root, nodes)



        
        