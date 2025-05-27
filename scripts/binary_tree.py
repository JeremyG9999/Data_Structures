class TreeNode:
    def __init__(self, data):
        self.data = data  
        self.left = None
        self.right = None
class TreeTraversal:
    def insert(self, root, data):
        if root is None:
            return TreeNode(data)
        else:
            if data < root.data:
                root.left = self.insert(root.left, data)
            else:
                root.right = self.insert(root.right, data)
        return root    
    def insertList(self, root, mylist):
        for data in mylist:
            root = self.insert(root, data)
        return root
    def inorderTraversal(self, root):
        result = []
        if root:
            result = self.inorderTraversal(root.left)
            result.append(root.data)
            result += self.inorderTraversal(root.right)
        return result
    def preorderTraversal(self, root):
        result = []
        if root:
            result.append(root.data)
            result += self.preorderTraversal(root.left)
            result += self.preorderTraversal(root.right)
        return result
    def postorderTraversal(self, root):
        result = []
        if root:
            result += self.postorderTraversal(root.left)
            result += self.postorderTraversal(root.right)
            result.append(root.data)
        return result
def main():
        tree = TreeTraversal()
        root = None
        elements = [5, 3, 7, 2, 4, 6, 8]
        root = tree.insertList(root, elements)
        # Inorder traversal
        sorted_elements = tree.inorderTraversal(root)
        print("\nInorder traversal:", sorted_elements)
        # Preorder traversal
        preorder_elements = tree.preorderTraversal(root)
        print("\nPreorder traversal:", preorder_elements)
        # Postorder traversal
        postorder_elements = tree.postorderTraversal(root)
        print("\nPostorder traversal:", postorder_elements)