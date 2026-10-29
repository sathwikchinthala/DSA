

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value, parent=None, side=None):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            print("Root inserted successfully")
            return

        p = self.search_node(parent)

        if p is None:
            print("Parent not found")
        elif side == "L":
            if p.left is None:
                p.left = new_node
                print("Node inserted successfully")
            else:
                print("Left child already exists")
        elif side == "R":
            if p.right is None:
                p.right = new_node
                print("Node inserted successfully")
            else:
                print("Right child already exists")
        else:
            print("Invalid side")

    def search_node(self, value):
        if self.root is None:
            return None

        q = deque([self.root])

        while q:
            node = q.popleft()

            if node.data == value:
                return node

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        return None

    def search(self, value):
        if self.search_node(value):
            print("Element found")
        else:
            print("Element not found")

    def display(self):
        if self.root is None:
            print("Tree is empty")
            return

        q = deque([self.root])
        print("Level-order traversal:", end=" ")

        while q:
            node = q.popleft()
            print(node.data, end=" ")

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        print()

    def delete(self, value):
        if self.root is None:
            print("Tree is empty")
            return

        if self.root.data == value:
            if self.root.left is None and self.root.right is None:
                self.root = None
                print("Leaf node deleted successfully")
            else:
                print("Cannot delete: Node is not a leaf")
            return

        q = deque([self.root])

        while q:
            node = q.popleft()

            if node.left:
                if node.left.data == value:
                    if node.left.left is None and node.left.right is None:
                        node.left = None
                        print("Leaf node deleted successfully")
                    else:
                        print("Cannot delete: Node is not a leaf")
                    return
                q.append(node.left)

            if node.right:
                if node.right.data == value:
                    if node.right.left is None and node.right.right is None:
                        node.right = None
                        print("Leaf node deleted successfully")
                    else:
                        print("Cannot delete: Node is not a leaf")
                    return
                q.append(node.right)

        print("Element not found")

    def preorder(self, node):
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")


bt = BinaryTree()

while True:
    print("\n1. Insert Root")
    print("2. Insert Child")
    print("3. Search")
    print("4. Display")
    print("5. Delete Leaf Node")
    print("6. Preorder")
    print("7. Inorder")
    print("8. Postorder")
    print("9. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        value = int(input("Enter root value: "))
        bt.insert(value)

    elif ch == 2:
        parent = int(input("Enter parent value: "))
        side = input("Enter side (L/R): ").upper()
        value = int(input("Enter child value: "))
        bt.insert(value, parent, side)

    elif ch == 3:
        value = int(input("Enter value to search: "))
        bt.search(value)

    elif ch == 4:
        bt.display()

    elif ch == 5:
        value = int(input("Enter leaf value to delete: "))
        bt.delete(value)

    elif ch == 6:
        print("Preorder:", end=" ")
        bt.preorder(bt.root)
        print()

    elif ch == 7:
        print("Inorder:", end=" ")
        bt.inorder(bt.root)
        print()

    elif ch == 8:
        print("Postorder:", end=" ")
        bt.postorder(bt.root)
        print()

    elif ch == 9:
        break

    else:
        print("Invalid choice")
