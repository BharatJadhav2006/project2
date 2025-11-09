def selection_sort(salaries):
    n = len(salaries)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if salaries[j] < salaries[min_index]:
                min_index = j
        # Swap the found minimum with the first element
        salaries[i], salaries[min_index] = salaries[min_index], salaries[i]
    return salaries

# --- Main Program ---
salaries = []

n = int(input("Enter number of employees: "))
for i in range(n):
    sal = float(input(f"Enter salary of employee {i + 1}: "))
    salaries.append(sal)

print("\nSalaries before sorting:")
print(salaries)

# Sorting using Selection Sort
selection_sort(salaries)

print("\nSalaries after sorting (Ascending Order):")
print(salaries)

# Display top five highest salaries
print("\nTop five highest salaries in the company:")
if n >= 5:
    for sal in salaries[-1:-6:-1]:   # last five elements in reverse
        print(sal)
else:
    print("Less than 5 employees, showing all salaries:")
    for sal in reversed(salaries):
        print(sal)
