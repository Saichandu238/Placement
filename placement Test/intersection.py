# 9. Write a Python func on to find the intersec on (common elements) of two lists.

def intersection(arr1,arr2):
    arr3=[]
    for i in range(len(arr1)):
        if arr1[i] in arr2:
            arr3.append(i)
    return arr3

arr1=[1,2,3,4,5]
arr2=[3,4,5,6,7]
intersection(arr1,arr2)
print(intersection(arr1,arr2))