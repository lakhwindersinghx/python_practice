#CHALLENGE 1
# x=[1,2,3,3,3,3,4,5, 1, 3, 5, 5, 5]
# y=[]
# def func(x,y):
#     for item in x:
#         if item not in y:
#             y.append(item)
#     return x,y
# func(x,y)
# unique_list=print(f'This is the unique list:{y} and original list: {x}')

#CHALLENGE 2
# a perfect number is one which is formed if we add it's divisors
#Divisors
# x=int(input("Enter your number:"))
# def divisors(x):
#     divisor = []
#     for i in range(1,(x)):
#
#         if x%i==0:
#             divisor.append(i)
#     print(f'These {divisor } are all the divisors of {x}')
#     return (divisor)
# # divisors((x))
# #perfect number:
# def perfect_number(x):
#     if sum(divisors(x))==x: #CALLED THE PREVIOUS FUNCTION HERE
#         print('Yes')
#         return True
#     else:
#         return False
# #Calling the function
# if perfect_number(x):
#     print(f'{x} is a perfect number')
# else:
#     print(f'{x} is not aa perfect number')

#CHALLENGE 3: Write a function that returns the factorial of a number n which is the function's argument.

# x=int(input('Enter the number:'))
# def factorial(x):
#     factorialx = 1
#     if x<0:
#         print('Please Enter a number greater than or equal 0')
#     else:
#         for number in range(1,x+1):
#             factorialx*=number
#     print(factorialx)
#     return
# factorial(x)

# CHALLENGE 4|Create a function that takes an integer as an argument and returns True if it’s a prime number and False otherwise.
# x=int(input('Enter a number:'))
# def prime(x):
#     for number in range(2,x):
#         if x%number==0:
#             return False
#         else:
#             return True
# if prime(x):
#     print(f'{x} is a prime number')
# else:
#     print(f'{x} is not a prime number')
#
# #CHALLENGE 5| Using the function defined in the previous challenge find 5 prime numbers greater than 1,000,000
# count = 0
# number = 1_000_001  # Start checking from 1,000,001
#
# while count < 5:
#     if prime(number):
#         print(number)
#         count += 1
#     number += 1

# CHALLENGE 5 FAIL

#CHALLENGE 6:
# x=int(input('Enter a number greater than 10:'))
#SOLUTION USING A WHILE LOOP
# def fibo(x):
#     if x<10:
#         print(f'The number you entered: {x} is smaller than 10, please re-enter.')
#     else:
#         a, b = 0, 1
#         while a <= x:
#             print(a,end='       ')
#             a, b = b, a + b
# fibo(x)
#SOLUTION USING A FOR LOOP
# a=0
# b=1
# for number in range(x+1):
#
#     print(a,end='   ')
#     a, b = b, a + b
#     if a>=x:
#         break

#CHALLENGE 7| EQUILIBRIUM INDEX
#I ACTUALLY COULDNT UNDERSTAND THE QUESTION BUT I STILL CAME UP WITH A SILLY SOLUTION.
# x=[-7, 1, 5, 2, -4, 2, 0]

# def equi(x):
#
#         if (sum(x[0:3]))==(sum(x[4:])):
#             print(f'{x}: is equilibrium index because: {sum(x[0:3])} is equal to{sum(x[4:])} ')
#         else:
#             print(f'{x}: is not equilibrium index because: {sum(x[0:3])} is not equal to{sum(x[4:])}')
#
# equi(x)

#THIS IS THE INSTRUCTOR'S SOLUTION TO THE PROBLEM
# def equilibrium_index(my_list):
#     for x in range(0,len(my_list)):
#         if sum(my_list[:x]) == sum(my_list[x+1:]):
#             return x
#
#     return False
#
# nums = [2, 3, 10, 5]
# print(equilibrium_index(nums))  # => 2
#
# nums = [3, 3, 10, 5]
# print(equilibrium_index(nums))

#CHALLENGE 8| SAME PROBLEM JUST A LITTLE MODIFICATION TO IT:
# def equilibrium_index(my_str):
#     my_list=my_str.split(',')
#     my_list=[int(n) for n in my_list]
#
#     for x in range(0,len(my_list)):
#         if sum(my_list[:x]) == sum(my_list[x+1:]):
#             return x
#     return False
# nums = '2, 3, 10, 5'
# print(equilibrium_index(nums))  # => 2
#
# nums = '2, 3, 10, 6'
# print(equilibrium_index(nums))

# CHALLENGE 9| MAKE A CHRISTMAS TREE
def tree(x):
    for i in range(1, x + 1):
        # print(i*'*')
        for j in range(x-i):
            print('$',end=' ')
        for j in range(2*i-1):
            print('*',end=' ')

        for j in range(x-i):
            print('$',end=' ')
        print() #UP UNTIL HERE IT'S PRINTING A TREE
    for i in range(x-1,0,-1): # THIS IS EXTRA FOR PRINTING A DIAMOND/ UPSIDE DOWN TREE
        for j in range(x -i):
            print('$', end=' ')
        for j in range(2*i - 1):
            print('*', end=' ')
        for j in range(x-i):
            print('$', end=' ')
        print()

tree(3)
#
