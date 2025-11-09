class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def search(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                return True
        return False

    def display(self):
        for i in range(self.size):
            print(i, ":", self.table[i])


# Main Program
ht = HashTable()

while True:
    print("\n1. Insert\n2. Search\n3. Delete\n4. Display\n5. Exit")
    ch = int(input("Enter your choice: "))
    
    if ch == 1:
        key = int(input("Enter key: "))
        value = input("Enter value: ")
        ht.insert(key, value)
    elif ch == 2:
        key = int(input("Enter key to search: "))
        val = ht.search(key)
        if val is not None:
            print("Value found:", val)
        else:
            print("Key not found.")
    elif ch == 3:
        key = int(input("Enter key to delete: "))
        if ht.delete(key):
            print("Key deleted successfully.")
        else:
            print("Key not found.")
    elif ch == 4:
        ht.display()
    elif ch == 5:
        break
    else:
        print("Invalid choice.")
