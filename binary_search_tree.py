class Node:
    def _init_(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def _init_(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        return root

    def search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def delete(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self.minValueNode(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        return root

    def minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

bst = BST()
while True:
    print("\n1.Insert\n2.Delete\n3.Search\n4.Display(Inorder)\n5.Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        key = int(input("Enter value to insert: "))
        bst.root = bst.insert(bst.root, key)
    elif ch == 2:
        key = int(input("Enter value to delete: "))
        bst.root = bst.delete(bst.root, key)
    elif ch == 3:
        key = int(input("Enter value to search: "))
        result = bst.search(bst.root, key)
        if result:
            print("Found")
        else:
            print("Not Found")
    elif ch == 4:
        print("Inorder Traversal: ", end="")
        bst.inorder(bst.root)
        print()
    elif ch == 5:
        break
    else:
        print("Invalid choice")
