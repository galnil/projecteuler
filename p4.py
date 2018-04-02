import ipdb 
import math

def is_palidrome(num):
    num = str(num)
    half_index_round_up = math.ceil(len(num) / 2)
    half_index_round_down = len(num) // 2
    first_half = num[:half_index_round_down]
    second_half = num[half_index_round_up:][::-1]
    return first_half == second_half

numbers = range(1000, 100, -1)

palindrome = 0

for i in numbers:
    for j in numbers:
        num = i * j
        if num < palindrome:
            break
        elif is_palidrome(num):
            palindrome = num

print(palindrome)
