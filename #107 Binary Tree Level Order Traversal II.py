'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        Do level order traversal, from bottom up
        Recursive solution. Level order top down, then reverse output
        """
        if root is None:
            return []
        curLevel = [root]
        result = []
        level = 0
        
        while curLevel:
            values = [node.val for node in curLevel]
            result.append(values)
            nextLevel = [c for nd in curLevel for c in [nd.left, nd.right] if c]
            curLevel = nextLevel

        return result[::-1]