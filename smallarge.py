# find largest and second largest DSA question
arr = [10, 3, 45, 6, 8, 23, 42, 56, 30]

largest = second_largest = arr[0]
smallest = second_smallest = arr[0]

for num in arr:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num < second_smallest and num != smallest:
        second_smallest = num

print("Largest element:", largest)
print("Second largest element:", second_largest)
print("Smallest element:", smallest)
print("Second smallest element:", second_smallest)
