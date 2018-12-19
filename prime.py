# finding prime numbers in a given array of numbers
import math
# specify range of values in which the prime numbers will be generated
max=int(input('find prime to which number?: '))
prime_list=[]

for x in range(2,max+1):
    isPrime=True
    for y in range(2,int(math.sqrt(x))+1):
        if x % y == 0:
            isPrime =False
            break
    if isPrime:
        prime_list.append(x)

print(prime_list)