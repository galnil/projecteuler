fib = [1, 1]

# generate the series until 1000000

while True:
    newval = fib[-1] + fib[-2]
    if newval > 1000000:
        break 
    fib.append(newval)

s = sum(fib)
print(s)
