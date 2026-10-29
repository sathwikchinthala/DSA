class BinaryTree:
    def __init__(self, size):
        self.tree = [None] * size
        self.size = size

    def insert(self, value, parent=None, side=None):
        if parent is None:
            if self.tree[0] is None:
                self.tree[0] = value
                print("Root inserted successfully")
            else:
                print("Root already exists")
            return

        if parent not in self.tree:
            print("Parent not found")
            return

        i = self.tree.index(parent)

        if side == "L":
            child = 2 * i + 1
        elif side == "R":
            child = 2 * i + 2
        else:
            print("Invalid side")
            return

        if child >= self.size:
            print("Array size exceeded")
        elif self.tree[child] is None:
            self.tree[child] = value
            print("Node inserted successfully")
        else:
            print("Position already occupied")

    def search(self, value):
        if value in self.tree:
            print("Element found at index", self.tree.index(value))
        else:
            print("Element not found")

    def display(self):
        print("Index\tNode")
        for i in range(self.size):
            if self.tree[i] is not None:
                print(i, "\t", self.tree[i])

    def delete(self, value):
        if value not in self.tree:
            print("Element not found")
            return

        i = self.tree.index(value)
        left = 2 * i + 1
        right = 2 * i + 2

        if ((left < self.size and self.tree[left] is not None) or
                (right < self.size and self.tree[right] is not None)):
            print("Cannot delete: Node is not a leaf")
        else:
            self.tree[i] = None
            print("Leaf node deleted successfully")

    def preorder(self, i=0):
        if i < self.size and self.tree[i] is not None:
            print(self.tree[i], end=" ")
            self.preorder(2 * i + 1)
            self.preorder(2 * i + 2)

    def inorder(self, i=0):
        if i < self.size and self.tree[i] is not None:
            self.inorder(2 * i + 1)
            print(self.tree[i], end=" ")
            self.inorder(2 * i + 2)

    def postorder(self, i=0):
        if i < self.size and self.tree[i] is not None:
            self.postorder(2 * i + 1)
            self.postorder(2 * i + 2)
            print(self.tree[i], end=" ")


n = int(input("Enter array size: "))
bt = BinaryTree(n)

while True:
    print("\n1.Insert Root")
    print("2.Insert Child")
    print("3.Search")
    print("4.Display")
    print("5.Delete Leaf Node")
    print("6.Preorder")
    print("7.Inorder")
    print("8.Postorder")
    print("9.Exit")

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
        bt.preorder()
        print()

    elif ch == 7:
        print("Inorder:", end=" ")
        bt.inorder()
        print()

    elif ch == 8:
        print("Postorder:", end=" ")
        bt.postorder()
        print()

    elif ch == 9:
        break

    else:
        print("Invalid choice")
