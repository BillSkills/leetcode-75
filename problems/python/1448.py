# [AC 07/06/2024]
# 1448. Count Good Nodes in Binary Tree
# Binary Tree -DFS
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(root, local_max):
            if not root: return
            if root.val >= local_max:
                self.res += 1
            local_max = max(local_max, root.val)

            dfs(root.left, local_max)
            dfs(root.right, local_max)

        dfs(root, root.val)
        return self.res