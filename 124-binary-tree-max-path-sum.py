# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):

    def maxPathSum(self, root):
        result = float('-inf')
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node):
            nonlocal result

            if node is None:
                return 0

            l = dfs(node.left)
            r = dfs(node.right)

            result = max(result, node.val + max(l, r, l + r, 0))

            return node.val + max(l, r, 0)

        dfs(root)
        return result
