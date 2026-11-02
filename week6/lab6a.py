
queue = []
size = int(input("Enter the size of queue: "))

front = 0

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        if len(queue) == size:
            print("Queue is Full")
        else:
            item = int(input("Enter the element to insert: "))
            queue.append(item)
            print(item, "inserted into queue")

    elif choice == 2:
        if len(queue) == 0:
            print("Queue is Empty")
        else:
            item = queue.pop(0)
            print("Deleted element:", item)

    elif choice == 3:
        if len(queue) == 0:
            print("Queue is Empty")
        else:
            print("Queue elements are:")
            for i in queue:
                print(i, end=" ")
            print()

    elif choice == 4:
        print("Exiting program")
        break

    else:
        print("Invalid choice")

