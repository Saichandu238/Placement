# 8. Write a program to show the two sorted lists, merge them into a single sorted list. 

def mergeList(arr1,arr2):
    l1=len(arr1)
    l2=len(arr2)
    arr3=[]
    j=0
    i=0
    # print(i,j)
    while i<l1 and j<l2:
        if(arr1[i]<arr2[j]):
            arr3.append(arr1[i])
            i+=1
        elif(arr1[i]>=arr2[j]):
             arr3.append(arr2[j]) 
             j+=1
    if(i!=l1 or j!=l2):
        while(i==l1 and j!=l2):
            arr3.append(arr2[j])
            j+=1
        while(i!=l1 and j==l2):
            arr3.append(arr1[i])
            i+=1

    print(arr3)
arr1=[1,2,3,4,5,6,7,8,9,55]
arr2=[2,4,5,6,7,8,10,15]
mergeList(arr1,arr2)