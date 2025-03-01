#3. Write a python function to check weather give number is prime or not

def prime(num):
    resu=True
    if(num<=1):
        return False
    for i in range(2,num):
        if(num%i==0):
            return False
    return True

num=int(input("Enter the number: "))
prime(num)
print(prime(num))

