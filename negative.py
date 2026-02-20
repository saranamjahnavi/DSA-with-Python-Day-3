arr = [-2,5,-1,3,0]
count=0
for i in range(len(arr)):
    if arr[i]<0:
        count+=1
print("No of negative numbers: ",count)