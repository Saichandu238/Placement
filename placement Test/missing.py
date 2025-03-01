# 5. Write a program to remove duplicates from a list while maintaining order. 

def missing(num):
    j=1
    for i in num:
        if j!=i:
            return j
        else:
            j+=1  
        
num=[1,2,4,5,6]
missing(num)
print(missing(num))