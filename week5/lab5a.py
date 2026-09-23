class STACK:
    def __init__(self):
        self.stack = []

    # Push operation
    def push(self, data):
        self.stack.append(data)
        print(data, "pushed into the stack.")

    # Pop operation
    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty. Stack is empty.")
        else:
            data = self.stack.pop()
            print(data, "popped from the stack.")

    # Peek operation
    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty.")
        else:
            print("Top element is:", self.stack[-1])

    # Display all elements
    def display(self):
        if len(self.stack) == 0:
            print("Stack is empty.")
        else:
            print("Stack elements are:")
            for i in range(len(self.stack) - 1, -1, -1):
                print(self.stack[i])

    # Count number of elements
    def count(self):
        print("Number of elements:", len(self.stack))


# Main program
s = STACK()

while True:
    print("\n----- STACK MENU -----")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Count")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter the element: "))
        s.push(data)

    elif choice == 2:
        s.pop()

    elif choice == 3:
        s.peek()

    elif choice == 4:
        s.display()

    elif choice == 5:
        s.count()

    elif choice == 6:
        print("Exiting program...")
        break

    else:
        print("Invalid choice.")
