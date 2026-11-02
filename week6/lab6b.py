
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(data, "inserted into queue")

    def dequeue(self):
        if self.front is None:
            print("Queue is Empty")
        else:
            print("Deleted element:", self.front.data)
            self.front = self.front.next
            if self.front is None:
                self.rear = None

    def display(self):
        if self.front is None:
            print("Queue is Empty")
        else:
            temp = self.front
            print("Queue elements:", end=" ")
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
            print()

q = Queue()

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = int(input("Enter the element to insert: "))
        q.enqueue(item)

    elif choice == 2:
        q.dequeue()

    elif choice == 3:
        q.display()

    elif choice == 4:
        print("Exiting program")
        break

    else:
        print("Invalid choice")

