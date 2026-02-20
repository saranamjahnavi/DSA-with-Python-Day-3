arr=[10,20,30,40,50]
sum=0
for i in range(len(arr)):
    if i%2==0:
        sum=sum+arr[i]
print("Sum :",sum)