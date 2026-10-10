arr = list(map(int, input("Enter elements of the array : ").split()))
largest = -1
for i in arr:
    if largest < i:
        largest = i
print(f"Largest element = {largest}")