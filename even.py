arr = [1,2,3,4,6]
count=0
for i in range(len(arr)):    #for i in arr:
    if arr[i]%2==0:
        count+=1                  #count=count+1
print("No.of even numbers: ",count)