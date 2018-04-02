"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def palindromic(num):
	if str(num) == str(num)[::-1]:
		return True
	else:
		return False


def main():
	palindromic_list = []
	for i in range(100, 1000):
		for ii in range(100, 1000):
			print('i: {0}, ii: {1}, ixii: {2}'.format(i,ii,i*ii))
			if palindromic(i*ii) == True:
				palindromic_list.append(i*ii)
			else:
				continue
	
	anwser = max(palindromic_list)
	print('anwser: {0}'.format(anwser))
if __name__ == '__main__':
	main()

