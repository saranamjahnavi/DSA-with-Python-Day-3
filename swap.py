arr = [1, 2, 3, 4, 5]
temp = arr[0]
arr[0] = arr[len(arr)-1]
arr[len(arr)-1] = temp
print("array after swapping first and last element:", arr)