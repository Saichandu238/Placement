# 7. Write a Python func on to count the number of vowels in a given string. 

def vowels(string):
    count=0
    v=['a','e','i','o','u','A','E','I','O','U']
    for i in (string):
        if i in v:
            count+=1
    return count

string=str(input("Enter the string: "))
vowels(string)
print(vowels(string))