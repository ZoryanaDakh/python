num1 = 0
num2 = 1
fib = [num1, num2]
fibs = num1 + num2
while fibs < 25:
    fib.append(fibs)
    num1 = num2
    num2 = fibs
    fibs = num1 + num2
print(fib)
    