class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_at_beginning(self, data):
        n = Node(data)

        if self.head is None:
            self.head = n
            n.next = self.head
            return

        temp = self.head

        # Find last node
        while temp.next != self.head:
            temp = temp.next

        n.next = self.head
        temp.next = n
        self.head = n

    # Insert at end
    def insert_at_end(self, data):
        n = Node(data)

        if self.head is None:
            self.head = n
            n.next = self.head
            return

        temp = self.head

        # Find last node
        while temp.next != self.head:
            temp = temp.next

        temp.next = n
        n.next = self.head

    # Insert at index
    def insert_at_index(self, data, index):
        if index < 0:
            print("Invalid index")
            return

        if index == 0:
            self.insert_at_beginning(data)
            return

        if self.head is None:
            print("No data Available")
            return

        new = Node(data)
        temp = self.head

        for i in range(index - 1):
            temp = temp.next

            if temp == self.head:
                print("Index out of range")
                return

        new.next = temp.next
        temp.next = new

    # Delete at beginning
    def delete_at_beginning(self):
        if self.head is None:
            print("No data Available")
            return

        # Only one node
        if self.head.next == self.head:
            self.head = None
            return

        temp = self.head

        # Find last node
        while temp.next != self.head:
            temp = temp.next

        self.head = self.head.next
        temp.next = self.head

    # Delete at end
    def delete_at_end(self):
        if self.head is None:
            print("No data Available")
            return

        # Only one node
        if self.head.next == self.head:
            self.head = None
            return

        temp = self.head

        # Find second-last node
        while temp.next.next != self.head:
            temp = temp.next

        temp.next = self.head

    # Remove node with value
    def remove_with_value(self, target):
        if self.head is None:
            print("No data Available")
            return

        # If first node contains target
        if self.head.data == target:
            self.delete_at_beginning()
            return

        temp = self.head

        while temp.next != self.head and temp.next.data != target:
            temp = temp.next

        if temp.next == self.head:
            print("No Value Present")
            return

        temp.next = temp.next.next

    # Count nodes
    def count(self):
        if self.head is None:
            print("Number of nodes: 0")
            return

        temp = self.head
        count = 0

        while True:
            count += 1
            temp = temp.next

            if temp == self.head:
                break

        print("Number of nodes:", count)

    # Display circular linked list
    def display(self):
        if self.head is None:
            print("No data available")
            return

        temp = self.head

        while True:
            print(temp.data, end=" -> ")
            temp = temp.next

            if temp == self.head:
                break

        print("(back to head)")


# Create circular linked list
l1 = CircularLinkedList()


# Menu
while True:
    print("\n========== CIRCULAR LINKED LIST MENU ==========")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Insert at Index")
    print("4. Delete at Beginning")
    print("5. Delete at End")
    print("6. Remove with Value")
    print("7. Count Nodes")
    print("8. Display")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter data: "))
        l1.insert_at_beginning(data)
        print("Node inserted at beginning.")

    elif choice == 2:
        data = int(input("Enter data: "))
        l1.insert_at_end(data)
        print("Node inserted at end.")

    elif choice == 3:
        data = int(input("Enter data: "))
        index = int(input("Enter index: "))
        l1.insert_at_index(data, index)

    elif choice == 4:
        l1.delete_at_beginning()
        print("First node deleted.")

    elif choice == 5:
        l1.delete_at_end()
        print("Last node deleted.")

    elif choice == 6:
        target = int(input("Enter value to remove: "))
        l1.remove_with_value(target)

    elif choice == 7:
        l1.count()

    elif choice == 8:
        l1.display()

    elif choice == 9:
        print("Program ended.")
        break

    else:
        print("Invalid choice. Try again.")
