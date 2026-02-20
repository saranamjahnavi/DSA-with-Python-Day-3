arr=[5,8,3,9]
target=3
found =False
for i in range(len(arr)):     
    if arr[i]==target:
        found =True
if found:
    print("Found")
else:
    print("Not found")