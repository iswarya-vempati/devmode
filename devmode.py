arr = list(map(int, input("Enter elements of the array : ").split())) # array initialization
largest = -1
for i in arr:
    if largest < i:
        largest = i
print(f"Largest element = {largest}")
