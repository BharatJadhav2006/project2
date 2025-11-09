class Node:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.prev = None
        self.next = None

class StudentList:
    def __init__(self):
        self.head = None

    def add_student(self, roll, name, marks):
        new_node = Node(roll, name, marks)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def display(self):
        if self.head is None:
            print("No records found.")
            return
        temp = self.head
        print("\nRoll\tName\tMarks")
        while temp:
            print(f"{temp.roll}\t{temp.name}\t{temp.marks}")
            temp = temp.next

    def sort_records(self, key, order):
        if self.head is None:
            print("No records to sort.")
            return
        swapped = True
        while swapped:
            swapped = False
            temp = self.head
            while temp.next:
                if key == "roll":
                    cond = temp.roll > temp.next.roll if order == "asc" else temp.roll < temp.next.roll
                else:
                    cond = temp.marks > temp.next.marks if order == "asc" else temp.marks < temp.next.marks
                if cond:
                    temp.roll, temp.next.roll = temp.next.roll, temp.roll
                    temp.name, temp.next.name = temp.next.name, temp.name
                    temp.marks, temp.next.marks = temp.next.marks, temp.marks
                    swapped = True
                temp = temp.next

# Main
obj = StudentList()

while True:
    print("\n1. Add Student")
    print("2. Display Records")
    print("3. Sort Records")
    print("4. Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        roll = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))
        obj.add_student(roll, name, marks)
    elif ch == 2:
        obj.display()
    elif ch == 3:
        key = input("Sort by (roll/marks): ").lower()
        order = input("Order (asc/desc): ").lower()
        obj.sort_records(key, order)
        print("Records sorted successfully.")
    elif ch == 4:
        break
    else:
        print("Invalid choice.")
