#searchelement
n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

search_element = int(input("Enter element to search: "))
found = False

for i in range(n):
    if arr[i] == search_element:
        print(f"Element found at index {i}")
        found = True
        break

if not found:
    print("Element not found")