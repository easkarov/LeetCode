# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """

        def dfs(node):
            if node is None:
                return 0

            if low <= node.val <= high:
                return dfs(node.left) + node.val + dfs(node.right)

            elif low > node.val:
                return dfs(node.right)
            elif high < node.val:
                return dfs(node.left)

        return dfs(root)