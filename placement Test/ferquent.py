# 2. Write a Python func on to find the most frequently occurring element in a list from collec ons import Counter 

def counter(arr):
    num=0
    max_count=0
    count=1
    j=0
    for i in arr:
        while(j<len(arr)-1):

            if(arr[i]==arr[j]):
                count+=1
                num=arr[i]
                j+=1
            else:
                j+=1
    if(count>max_count):
        max_count=count
    return num
arr=[1,3,4,5,2,4,2,2,3,3,3,3,34]
print(counter(arr))
