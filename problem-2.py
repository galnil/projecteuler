"""
problem:
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

"""
answer: ----
"""
def F(bound):
    a,b = 0,1
    while a <= bound:
        yield a
        a, b = b, a + b

def fib(n):
	if n == 0: return 0
	elif n == 1: return 1
	else: return fib(n-1)+fib(n-2)

def main():
	# test
	first_10 = [fib(n) for n in range(10)]
	print(first_10)

	fib_list = [i for i in F(4*10**6) if i % 2 == 0]
	# print out answer
	print(sum(fib_list))
	

if __name__ == '__main__':
	main()
