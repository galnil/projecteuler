max_number = 1000

mul_of_3 = list(range(0, max_number, 3))
mul_of_5 = list(range(0, max_number, 5))
mul_of_15 = list(range(0, max_number, 3 * 5))

s = sum(mul_of_3) + sum(mul_of_5) - sum(mul_of_15)
print(s)
