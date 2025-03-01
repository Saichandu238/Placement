# 6.Write a Python program to find the second largest number in a list. 

def secondLargest(arr):
    max=0
    second_max=0
    for i in range(0,len(arr)):
        if arr[i]>second_max and arr[i]>max:
            second_max=max
            max=arr[i]
        
    return second_max

arr=[1,2,3,4,5,9,10,12,3,4,5]
secondLargest(arr)
print(secondLargest(arr))