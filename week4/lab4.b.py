class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_at_beginning(self, data):
        n = Node(data)

        if self.head is None:
            self.head = n
            return

        n.next = self.head
        self.head.prev = n
        self.head = n

    # Insert at end
    def insert_at_end(self, data):
        n = Node(data)

        if self.head is None:
            self.head = n
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = n
        n.prev = temp

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
            if temp.next is None:
                print("Index out of range")
                return

            temp = temp.next

        new.next = temp.next
        new.prev = temp

        if temp.next:
            temp.next.prev = new

        temp.next = new

    # Delete at beginning
    def delete_at_beginning(self):
        if self.head is None:
            print("No data Available")
            return

        self.head = self.head.next

        if self.head:
            self.head.prev = None

    # Delete at end
    def delete_at_end(self):
        if self.head is None:
            print("No data Available")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.prev.next = None

    # Remove node with value
    def remove_with_value(self, target):
        if self.head is None:
            print("No data Available")
            return

        temp = self.head

        # If first node contains target
        if temp.data == target:
            self.delete_at_beginning()
            return

        while temp and temp.data != target:
            temp = temp.next

        if temp is None:
            print("No Value Present")
            return

        # If deleting last node
        if temp.next is None:
            temp.prev.next = None
            return

        # Middle node
        temp.prev.next = temp.next
        temp.next.prev = temp.prev

    # Count nodes
    def count(self):
        temp = self.head
        count = 0

        while temp:
            count += 1
            temp = temp.next

        print("Number of nodes:", count)

    # Display forward
    def display(self):
        if self.head is None:
            print("No data available")
            return

        temp = self.head

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")

    # Display backward
    def display_reverse(self):
        if self.head is None:
            print("No data available")
            return

        temp = self.head

        # Go to last node
        while temp.next:
            temp = temp.next

        # Traverse backwards
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev

        print("None")


# Create doubly linked list
l1 = DoublyLinkedList()


# Menu
while True:
    print("\n========== DOUBLY LINKED LIST MENU ==========")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Insert at Index")
    print("4. Delete at Beginning")
    print("5. Delete at End")
    print("6. Remove with Value")
    print("7. Count Nodes")
    print("8. Display Forward")
    print("9. Display Reverse")
    print("10. Exit")

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
        l1.display_reverse()

    elif choice == 10:
        print("Program ended.")
        break

    else:
        print("Invalid choice. Try again.")
