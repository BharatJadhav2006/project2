# Initialize customer list
custids = []

# Function to add a customer
def addcustomer(custids, custid=0):
    if custid <= 0:
        print("Invalid customer ID")
        return
    custids.append(custid)
    print(f"Added customer ID: {custid}")

# Add customers
n = int(input("Enter number of customers to add: "))
for i in range(n):
    cid = int(input(f"Enter customer ID {i+1}: "))
    addcustomer(custids, cid)

print("\nCustomer List:", custids)

# ---------------- LINEAR SEARCH ----------------
def linear_search(custids, key):
    print("\n#### LINEAR SEARCH ####")
    t = 0
    for i in range(len(custids)):
        t += 1
        print(f"Comparing {custids[i]} with key {key} | Time: {t}")
        if custids[i] == key:
            print("-" * 50)
            print(f"Customer ID {key} exists (Time: {t})")
            return
    print("-" * 50)
    print(f"Customer ID {key} does not exist (Time: {t})")

# Perform linear search
key = int(input("\nEnter customer ID to search (Linear): "))
linear_search(custids, key)

# ---------------- BINARY SEARCH ----------------
def binary_search(cust_list, key, low=0, high=None, t=1):
    if high is None:
        high = len(cust_list) - 1
    if low > high:
        print("-" * 50)
        print(f"Customer ID {key} does not exist (Time: {t})")
        return
    mid = (low + high) // 2
    print(f"Comparing {cust_list[mid]} with key {key} | Time: {t}")
    if cust_list[mid] == key:
        print("-" * 50)
        print(f"Customer ID {key} exists (Time: {t})")
        return
    elif cust_list[mid] > key:
        binary_search(cust_list, key, low, mid - 1, t + 1)
    else:
        binary_search(cust_list, key, mid + 1, high, t + 1)

# Sort and perform binary search
cust_list = sorted(custids)
print("\nSorted List for Binary Search:", cust_list)
key = int(input("Enter customer ID to search (Binary): "))
binary_search(cust_list, key)

Algorithm

1. Linear Search Algorithm

1. Start from the first element of the list.


2. Compare each element with the target ID.


3. If a match is found, return its position.


4. If the end of the list is reached and no match is found, return “Not Found”.



2. Binary Search Algorithm

1. Sort the list in ascending order.


2. Set low = 0 and high = len(list) - 1.


3. Find the middle index mid = (low + high) // 2.


4. If list[mid] == target, return “Found”.


5. If list[mid] > target, set high = mid - 1.


6. Else, set low = mid + 1.


7. Repeat until low > high.


8. If not found, return “Not Found”.

