arr=[1,2,2,3,1,4,3]
remove=[]
for i in range(len(arr)):
    if arr[i]!=2:
        remove.append(arr[i])
print("Array :",remove)