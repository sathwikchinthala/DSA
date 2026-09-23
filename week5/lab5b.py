# Program to implement Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LINKEDLIST:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(data, "inserted at beginning.")

    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head

            while temp.next is not None:
                temp = temp.next

            temp.next = new_node

        print(data, "inserted at end.")

    # Delete from beginning
    def delete_beginning(self):
        if self.head is None:
            print("Linked List is empty.")
        else:
            data = self.head.data
            self.head = self.head.next
            print(data, "deleted from beginning.")

    # Delete from end
    def delete_end(self):
        if self.head is None:
            print("Linked List is empty.")

        elif self.head.next is None:
            data = self.head.data
            self.head = None
            print(data, "deleted from end.")

        else:
            temp = self.head

            while temp.next.next is not None:
                temp = temp.next

            data = temp.next.data
            temp.next = None
            print(data, "deleted from end.")

    # Display linked list
    def display(self):
        if self.head is None:
            print("Linked List is empty.")
        else:
            temp = self.head

            print("Linked List elements are:")

            while temp is not None:
                print(temp.data, end=" -> ")
                temp = temp.next

            print("None")

    # Count number of elements
    def count(self):
        count = 0
        temp = self.head

        while temp is not None:
            count += 1
            temp = temp.next

        print("Number of elements:", count)


# Main program
l = LINKEDLIST()

while True:
    print("\n----- LINKED LIST MENU -----")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Delete from Beginning")
    print("4. Delete from End")
    print("5. Display")
    print("6. Count")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter the element: "))
        l.insert_beginning(data)

    elif choice == 2:
        data = int(input("Enter the element: "))
        l.insert_end(data)

    elif choice == 3:
        l.delete_beginning()

    elif choice == 4:
        l.delete_end()

    elif choice == 5:
        l.display()
