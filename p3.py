import ipdb
import sys
import math 

def find_prime_factor(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return num / i, i
    return 1, num

def main():
    num = float(sys.argv[1])

    while num != 1:
        num, prime_facor = find_prime_factor(num)
    
    return prime_facor

print(main())
