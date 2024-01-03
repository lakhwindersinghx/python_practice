# x=int(input('Enter a number:'))
def prime(x):
    for number in range(2,x):
        if x%number==0:
            return False
        else:
            return True
def prime_greater(x):
    count = 0
    number = 1_000_001  # Start checking from 1,000,001

    while count < 5:
        if prime(number):
            print(number)
            count += 1
            number += 1
prime