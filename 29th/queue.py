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

    def level_order_traversal(self):
        if self.root is None:
            return []
       
        result = []
        queue = [self.root]
       
        while queue:
            current_level_size = len(queue)
            current_level = []
           
            for _ in range(current_level_size):
                node = queue.pop(0)
                current_level.append(node.val)
               
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                   
            result.append(current_level)
       
        return result

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

# Perform level order traversal and print results
levels = bst.level_order_traversal()

print("Level order traversal of the BST:")
for level in levels:
    print(" ".join(map(str, level)))