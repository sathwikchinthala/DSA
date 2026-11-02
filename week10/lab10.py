
SIZE = 10

# Hash Table
chaining = [[] for i in range(SIZE)]
linear = [None] * SIZE
quadratic = [None] * SIZE

# Hash Function
def hash_function(key):
    return key % SIZE

# Separate Chaining
def chain_insert(key):
    pos = hash_function(key)
    if key not in chaining[pos]:
        chaining[pos].append(key)
        print("Element inserted successfully")
    else:
        print("Element already exists")

def chain_search(key):
    pos = hash_function(key)
    if key in chaining[pos]:
        print("Element found at index", pos)
    else:
        print("Element not found")

def chain_display():
    print("Hash Table using Separate Chaining:")
    for i in range(SIZE):
        print(i, ":", chaining[i])


# Linear Probing
def linear_insert(key):
    pos = hash_function(key)

    for i in range(SIZE):
        index = (pos + i) % SIZE
        if linear[index] is None:
            linear[index] = key
            print("Element inserted at index", index)
            return
        if linear[index] == key:
            print("Element already exists")
            return

    print("Hash Table is Full")

def linear_search(key):
    pos = hash_function(key)

    for i in range(SIZE):
        index = (pos + i) % SIZE

        if linear[index] is None:
            break
        if linear[index] == key:
            print("Element found at index", index)
            return

    print("Element not found")

def linear_display():
    print("Hash Table using Linear Probing:")
    for i in range(SIZE):
        print(i, ":", linear[i])


# Quadratic Probing
def quadratic_insert(key):
    pos = hash_function(key)

    for i in range(SIZE):
        index = (pos + i * i) % SIZE

        if quadratic[index] is None:
            quadratic[index] = key
            print("Element inserted at index", index)
            return
        if quadratic[index] == key:
            print("Element already exists")
            return

    print("Hash Table is Full")

def quadratic_search(key):
    pos = hash_function(key)

    for i in range(SIZE):
        index = (pos + i * i) % SIZE

        if quadratic[index] is None:
            break
        if quadratic[index] == key:
            print("Element found at index", index)
            return

    print("Element not found")

def quadratic_display():
    print("Hash Table using Quadratic Probing:")
    for i in range(SIZE):
        print(i, ":", quadratic[i])


# Main Menu
while True:
    print("\n===== HASHING TECHNIQUES =====")
    print("1. Separate Chaining")
    print("2. Linear Probing")
    print("3. Quadratic Probing")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 4:
        print("Program terminated.")
        break

    if choice not in [1, 2, 3]:
        print("Invalid choice")
        continue

    while True:
        print("\n1. Insert")
        print("2. Search")
        print("3. Display")
        print("4. Back to Main Menu")

        operation = int(input("Enter your operation: "))

        if operation == 4:
            break

        if operation == 1:
            key = int(input("Enter element to insert: "))

            if choice == 1:
                chain_insert(key)
            elif choice == 2:
                linear_insert(key)
            else:
                quadratic_insert(key)

        elif operation == 2:
            key = int(input("Enter element to search: "))

            if choice == 1:
                chain_search(key)
            elif choice == 2:
                linear_search(key)
            else:
                quadratic_search(key)

        elif operation == 3:
            if choice == 1:
                chain_display()
            elif choice == 2:
                linear_display()
            else:
                quadratic_display()

        else:
            print("Invalid operation")
