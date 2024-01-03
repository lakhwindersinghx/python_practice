# # Write a Python function that takes a list as an argument and returns a new list with unique elements of the first list in the same order.
# # #
# # # Sample List : [1,2,3,3,3,3,4,5, 1, 3, 5, 5, 5]
# # # Unique List : [1, 2, 3, 4, 5]
# # sample_List=[1,2,3,3,3,3,4,5, 1, 3, 5, 5, 5]
# # unique_list=[]
# # for item in sample_List:
# #     if item not in unique_list:
# #         unique_list.append((item))
# # print(unique_list)
#
# # Write a Python function to check whether a number is perfect or not.
# # The function should return True if the number is perfect and False otherwise.
#
# # x=int(input('Enter:'))
# # def divisors(x):
# #     divs=[]
# #     for number in range(1,int(x/2)+1):
# #         if x%number==0:
# #             divs.append(number)
# #     return divs
# #
# # def perfect(x):
# #     perfecto=divisors(x)
# #     if sum(perfecto)==x:
# #         return True
# #     else:
# #         return False
# # if perfect(x):
# #     print(f'The number you entered:{x} is a perfect number')
# # else:
# #     print((f'The number you entered: {x} is not a perfect number'))
#
# # #CHALLENGE-3 Write a function that returns the factorial of a number n which is the function's argument.
# # def factorial(n):
# #     facto=1
# #     for number in range(1,n+1):
# #         facto*=number
# #     print(facto)
# #
# # factorial(n=5)
#
#Challenge-4 Create a function that takes an integer as an argument and returns True if it’s a prime number and False otherwise.


#CHALLENGE 5 SKIP
#CHALLENGE 6:Write a function called fibo that takes an integer greater than 10 as an argument
# and returns the Fibonacci series between 0 and the function's argument.
# def fibo(x):
#     if x<10:
#         print(f'The number you entered: {x} is smaller than 10, please re-enter.')
#     else:
#         a, b = 0, 1
#         while a <= x:
#             print(a,end='       ')
#             a, b = b, a + b
# fibo(x=int(input('Enter a number: ')))

#CHALLENGE-9:
def draw_tree(n):
    count=0 #straight tree
    for number in range(1,n+1):
        number+=count
        count += 1
        print('*'*number)
