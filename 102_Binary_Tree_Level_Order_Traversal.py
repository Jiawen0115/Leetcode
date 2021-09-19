#Question:	Given the root of a binary tree, return the level order traversal 
#			of its nodes' values. (i.e., from left to right, level by level).
#Author: Jiawen Liu

# Definition for a binary tree node.
#class TreeNode(object):
     #def __init__(self, val=0, left=None, right=None):
        #self.val = val
        #self.left = left
        #self.right = right
    
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        tree = []
        if not root:
            return tree
        if not root.left and not root.right:
            tree.append([root.val])
        else:
            nodes = [[root,0]]
            while(nodes): 
                node,level = nodes.pop(0)
                if len(tree) <= level:
                    tree.append([])
                tree[level].append(node.val)
                if node.left:
                    nodes.append([node.left,level+1])
                if node.right:
                    nodes.append([node.right,level+1])
        return tree
                
