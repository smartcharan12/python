class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)

    def inorder_traversal(self, node):
        
        if node:
             self.inorder_traversal(node.left)
             print(node.val)
             self.inorder_traversal(node.right)
    def height(self,root):
        if root is None:
            return 0
        leftheight=self.height(root.left)
        rightheight=self.height(root.left)
        return (max(leftheight,rightheight)+1)
    def decend(self, node):
        
        if node:
            self.decend(node.right)
            
            print(node.val)
            self.decend(node.left)
    def _search(self,node,key):
        if node is None : 
         return None
        if node.val == key:
            return node
        if key<node.val:
            return self._search(node.left,key)
        else :
            return self._search(node.right,key)  
# Function to take user input and create the BST
def create_bst_from_input():
    bst = BinarySearchTree()
    elements = input("Enter the elements to insert into the BST, separated by space: ").split()
    elements = list(map(int, elements))  # Convert input to list of integers

    for element in elements:
        bst.insert(element)

    return bst

# Create BST from user input
bst = create_bst_from_input()

# Display the elements of the BST in sorted order
print("Inorder traversal of the BST:", bst.inorder_traversal(bst.root))
bst.decend(bst.root)
#input must be inline
print(bst.height(bst.root))
if  bst._search(bst.root,16):
    print("found")
else:
    print("not found")