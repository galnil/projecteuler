"""
problem:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

"""
answer --> 233168
"""

def ceildiv(a, b):
	return -(-a // b)

def f(multiples=[], bound=0):
	
	target = set()
	for m in multiples:
		for n in range(ceildiv(bound, m)):
			target.add(n*m)



def main():
	target = f([3, 5], 1000)
	print(sum(target))

if __name__ == '__main__':
	main()
