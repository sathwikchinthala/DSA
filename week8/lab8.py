tree = []

def insert(value):
    global tree
    if len(tree) == 0:
        tree.append(value)
        print("Inserted successfully")
        return

    i = 0
    while i < len(tree):
        if tree[i] == -1:
            tree[i] = value
            print("Inserted successfully")
            return
        elif value < tree[i]:
            i = 2 * i + 1
        elif value > tree[i]:
            i = 2 * i + 2
        else:
            print("Duplicate value not allowed")
            return

        while i >= len(tree):
            tree.append(-1)

    tree.append(value)


def search(value):
    i = 0
    while i < len(tree) and tree[i] != -1:
        if tree[i] == value:
            return True
        elif value < tree[i]:
            i = 2 * i + 1
        else:
            i = 2 * i + 2

    return False


def inorder(i):
    if i < len(tree) and tree[i] != -1:
        inorder(2 * i + 1)
        print(tree[i], end=" ")
        inorder(2 * i + 2)


def preorder(i):
    if i < len(tree) and tree[i] != -1:
        print(tree[i], end=" ")
        preorder(2 * i + 1)
        preorder(2 * i + 2)


def postorder(i):
    if i < len(tree) and tree[i] != -1:
        postorder(2 * i + 1)
        postorder(2 * i + 2)
        print(tree[i], end=" ")


while True:
    print("\n\n1. Insert")
    print("2. Search")
    print("3. Inorder")
    print("4. Preorder")
    print("5. Postorder")
    print("6. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        value = int(input("Enter value: "))
        insert(value)

    elif ch == 2:
        value = int(input("Enter value to search: "))
        if search(value):
            print("Value found")
        else:
            print("Value not found")

    elif ch == 3:
        print("Inorder:")
        inorder(0)

    elif ch == 4:
        print("Preorder:")
        preorder(0)

    elif ch == 5:
        print("Postorder:")
        postorder(0)

    elif ch == 6:
        print("Program terminated")
        break

    else:
        print("Invalid choice")
