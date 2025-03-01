# 4. Write a program to remove duplicates from a list while maintaining order. 

def duplicates(arr):
    left=0
    # print(left)
    right=len(arr)-1
    while left<right:
        print(arr[left])
        print(arr[right])
        if(arr[left]==arr[right]):
            arr.append(0)
            # left+=1
            right-=1
        else:
            # left+=1
            right-=1
        # left+=1
        
    return arr

arr=[1,2,3,4,5,64,6,3]
duplicates(arr)
print(duplicates(arr))