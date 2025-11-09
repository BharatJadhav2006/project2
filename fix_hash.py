# Hash Table Implementation using Linear Probing
SIZE = 10  # Fixed size

class HashTable:
    def __init__(self):
        self.table = [None] * SIZE

    def hash_function(self, key):
        return key % SIZE

    def insert(self, key):
        index = self.hash_function(key)
        start_index = index  # remember starting point for full table check

        while self.table[index] is not None and self.table[index] != "DELETED":
            index = (index + 1) % SIZE
            if index == start_index:
                print("Hash Table is Full!")
                return
        self.table[index] = key
        print(f"Inserted key {key} at index {index}")

    def search(self, key):
        index = self.hash_function(key)
        start_index = index

        while self.table[index] is not None:
            if self.table[index] == key:
                print(f"Key {key} found at index {index}")
                return
            index = (index + 1) % SIZE
            if index == start_index:
                break


      Algorithm (Step-by-Step)

1️⃣ Hash Function:
→ Find index using
index = key % size

2️⃣ Insert Key:
→ If the place is empty → put it there.
→ If not empty → move one step ahead (linear probing).

3️⃣ Search Key:
→ Start at hash index → move ahead until you find it or reach empty slot.

4️⃣ Delete Key:
→ Search the key → replace it with "DELETED".

5️⃣ Display Table:
→ Show all elements in the hash table.
