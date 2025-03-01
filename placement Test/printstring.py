# 10. Write a program to print a string, find the first non-repea ng character. 

def string(str1):
    print(str1)
    i=0
    j=1
    res=True
    while(i<len(str1) and j<len(str1)):
        if(str1[i]==str1[j]):
            res=False
            j+=1
            i+=1
        else:
            j+=1
        # return
    
    if(res):
        print(str1[i])
str1=str(input("Enter the string: "))
string(str1)