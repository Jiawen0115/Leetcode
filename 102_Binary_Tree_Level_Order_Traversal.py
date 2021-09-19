#Question:	Given the root of a binary tree, return the level order traversal 
#			of its nodes' values. (i.e., from left to right, level by level).
#Author: Jiawen Liu

# Definition for a binary tree node.
#class TreeNode(object):
     #def __init__(self, val=0, left=None, right=None):
        #self.val = val
        #self.left = left
        #self.right = right
    
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        tree = []
        if not root:
            return tree
        if not root.left and not root.right:
            tree.append([root.val])
        else:
            nodes = [root]
            level = 0
            while(nodes): #Pop nodes for every level, and add nodes in queue for next level
						  #Every where a node is null, put None in queue 
                level_values = []
                if len(nodes) < 2**level+1:
                    temp = nodes 
                    nodes = []
                else:
                    temp = nodes[:2**level+1]
                    del nodes[:2**level+1]
                for item in temp:
                    if item:
                        level_values.append(item.val)
                        nodes.extend([item.left,item.right])
                    else:
                        nodes.extend([None,None])
                if not level_values:
                    break
                level += 1
                tree.append(level_values)
        return tree
                
