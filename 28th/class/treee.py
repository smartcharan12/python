class TreeNode:
    def __init__ (self,key):
        self.left=None
        self.right=None
        self.val=key
    def inorder(self,root) :
     if root==None:
      return 
     self.inorder(root.left)
     print(root.val)
     self.inorder(root.right)

#Creating the node
root=TreeNode(1)
#adding children
root.left=TreeNode(2)

root.right=TreeNode(3)
#addinjg grandchildren
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)

root.inorder(root)