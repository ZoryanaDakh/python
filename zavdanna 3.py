import random

randnumber = random.randint(0, 20)

while True:
    num = int (input('Відгадай задумане число'))
    randnumber == num
    if num < randnumber:
        print ('моє число більше!')
    elif num > randnumber:
        print ('моє число менше!')
    else:
        print ('молодець! ти відгадав!')
        break