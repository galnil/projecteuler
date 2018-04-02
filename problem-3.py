"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
from math import sqrt

factor_list = list()

def prime_factors(num):
	local_factor_list = list()
	i = 2
	while i <= int(sqrt(num)):
		if num % i == 0:
			local_factor_list.append(i)
			factor_list.extend(local_factor_list)
			print("num: {0}, i: {1}, num/i: {2} ".format(num, i, num/ i))
			num = num / i
			prime_factors(num)
			break
		i += 1
		if ( i == int(sqrt(num)) ) and ( local_factor_list == list() ):
			print('{0} is prime'.format(num))
			local_factor_list.append(int(num))
			factor_list.extend(local_factor_list)
			break
	return factor_list

def main():
	"""
	factor_list = prime_factors(13195) # [5,7,13,29]
	print( " factor list: {0} ".format(max(factor_list)) ) # 29
	
	
	"""

	n = 600851475143
	factor_list = prime_factors(n)
	print('anwser: {0}'.format( max(factor_list) )) #6587
if __name__ == '__main__':
	main()
