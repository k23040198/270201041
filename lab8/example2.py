def is_prime(num):
    prime=True
    for i in range(2,int((num**0.5)+1)):
        if num%i==0:
            prime=False
        elif num==0 or  num==1:
            prime=False
    return prime
    
def print_primes_between():
    list=[]
    number1=int(input("Please enter the number "))
    number2=int(input("Please enter the number "))
    for i in range(number1+1,number2):
        if is_prime(i)==True and i!=1:
            list.append(i)
    print(list)
print_primes_between()