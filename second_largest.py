arr = list(map(int, input("Enter elements of the array : ").split()))
largest = second_largest = -1
for i in arr:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i
print(f"Second largest element = {second_largest}")