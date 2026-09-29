#calculate array
nums= []
sum = 0
n = int(input("enter size of array:"))
for i in range(n):
    num = int(input(f"enter {i}element of array:"))
    nums.append(num)
    sum += nums[i]
print(sum)   