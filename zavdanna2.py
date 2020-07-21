num1 = 0
num2 = 1
fib = [num1, num2]
fibs = num1 + num2

while fibs < 100:
    fib.append(fibs)
    num1 = num2
    num2 = fibs
    fibs = num1 + num2
while True:
    num = int(input('Введи число'))
    if num in fib:
        print ('задача оцінена в ',num,' балів')
    else:
        print('Введіть коректне число')
    