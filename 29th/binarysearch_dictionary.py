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
            if key > node.val:  # Ensure no duplicate values
                if node.right is None:
                    node.right = TreeNode(key)
                else:
                    self._insert(node.right, key)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.val)
            self.inorder_traversal(node.right)

# Function to take multiple strings input and insert them into the BST
def create_bst_from_input():
    bst = BinarySearchTree()
    print("Enter strings to insert into the BST (type 'done' to finish):")
    while True:
        string = input()
        if string.lower() == 'done':
            break
        bst.insert(string)
    return bst

# Create BST from user input
bst = create_bst_from_input()
print("in order transvers: ")

# Perform in-order traversal to get strings in dictionary order

bst.inorder_traversal(bst.root)

 