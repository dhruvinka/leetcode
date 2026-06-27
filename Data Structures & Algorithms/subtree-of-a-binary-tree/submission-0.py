# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):

    def isIdentical(self,root,subRoot):
        if not root or not subRoot:
            return root == subRoot
        
        return root.val == subRoot.val and self.isIdentical(root.left,subRoot.left) and self.isIdentical(root.right,subRoot.right)



    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        if not root or not subRoot:
            return root == subRoot

        if root.val == subRoot.val  and self.isIdentical(root,subRoot):
            return True

        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)