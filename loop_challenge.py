#CHALLENGE-1: Create a Python script that asks the user for a number and
# then prints out a list of all the divisors of each number less than the asked number.
import string

# x=int(input('enter a number:'))
# y_list=[]
# for number in range(1,x//2+1):
#     if x%number==0:
#         y_list.append(number)
# print(y_list)

#CHALLENGE 2-Write a Python program to check if an integer (x) is
# the power of another integer (y). Prompt the user to input both integers.
# x = int(input("Enter a number x: "))
# y = int(input(f"Enter a number y to test if x which is {x} is a power of y: "))
#
# found = False
#
# for k in range(2, x//2):
#     if y ** k == x:
#         print(f"{y} ** {k} = {x}")
#         found = True
#         break
# else:
#     print(f'{x} is not the power of {y}')

#CHALLENGE 3:Write a Python program that counts and displays the vowels of a given string ignoring the letter case.
# x=input('Enter your sentence:').lower()
# vowels='aeiou'
# count=0
# for word in x:
#     if word in vowels:
#         count+=1
# print(count)
#CHALLENGE 4: NOT DOING (Write a Python script that checks if a triangle is equilateral, isosceles or scalene.)

#CHALLENGE 5: Write a Python program that calculates and displays the sum,
# the product and the average of n float numbers entered by the user, each on a separate line.
# Enter 0 to finish
#
# print('Enter floats to calculate or press 0 to exit.')
# count=0
# sum=0
# product=1
# while True:
#     num = float(input('Enter a float number:'))
#     if num==0:
#         break
#     else:
#         sum+=num
#         product*=num
#         count+=1
#     if count<2:
#         print(f'Enter some more floats')
#     else:
#         print(f'Float you entered:{num}. \n1.It\'s sum: {sum} \n2.It\'s product: {product} \n3.It\'s average: {sum/count}')

#CHALLENGE-6:Given the string s1, write a program to return the sum
#and the average of the digits that appear in the string,
#ignoring all other characters.
# s1='Python31py50'
#
# sum=0
# count=0
# x=string.digits
# for number in s1:
#     if number in x:
#         sum+=int(number)
#         count+=1
# print(f'Hence the sum: {sum} and the average: {sum/count}')

#Challenge-7
#Write a Python program that displays the multiplication table (from 1 to 10) of a specific integer number entered by the user.
# x=int(input('enter a number:'))
# for number in range (0,11):
#     print(x*number)


#Write a Python script that displays the following pattern from 1 to n where n is entered by the user.
# x=int(input('Enter a number:'))
# count=0
# for number in range(1,x+1):
#     count+=1
#     print(str(number)*count)

#######################################################################################################
#SECOND SOLUTION

# x=int(input('Enter a number:'))
# count=0
# while count<=x:
#     for number in range(x+1):
#         print(str(number)*count)
#         count += 1
#     break

#CHALLENGE-9: Write a Python program that finds the common characters that appear in two given strings.
# x=input('Enter sentence 1:')  #SOLUTION-1
# y=input('Enter sentence 2:')
# list(x)
# list(y)
# z=[]
# for word in x:
#     if word in y:
#         z.append(word)
# k=''.join(z)
# print(f'Hence, the characters common in both the strings: {k}')
#######################################################################################################
#SOLUTION-2 (KINDA DIFFERENT SOLUTION BUT I LIKE THE EARLIER ONE BETTER)
# x='I am a good boy'
# y='I am a bad boy'
# z=string.ascii_letters
# j=''
# for word in x:
#     if word in y:
#         if word not in j:
#             j+=word
# print(f'Hence, the common characters are: {j}')

#CHALLENGE-10: FOOBAR CHALLENGE:
# Write a Python program that iterates over the integers from 1 to 50.
# For multiples of three print "Foo" instead of the number and for multiples of five print "Bar".
# For numbers that are multiples of both three and five print "FooBar".

# for word in range(1,51):
#     if word%3==0 and word%5==0:
#         print('FooBar')
#     if word%3==0:
#         print('Foo')
#     if word%5==0:
#         print('Bar')
#SOLUTION -2: SAME COULD BE DONE WITH A WHILE LOOP AS WELL

# count=0
# while count<50:
#     count += 1
#     if count % 3 == 0 and count % 5 == 0:
#         print(count,('FooBar'))
#     if count%3==0:
#         print(count,('Foo'))
#     if count%5==0:
#         print(count, ('Bar'))

#CHALLENGE-11: Write a Python script that prints out the Fibonacci series up to a given number n.
#Example: if n is 23 it will print out 0, 1, 1, 2, 3, 5, 8, 13, 21

# x=int(input('Enter a number:'))
# z,y=0,1
# while z<=x:
#     print(z,'',end=' ')
#     z,y=y,z+y
# print(z,y)

#CHALLENGE-12: STAR TREE

# n=5
# count=0
# for number in range(n+1):
#     count+=1
#     print('*'*count)
# for number in range(n):
#     count-=1
#     print('*'*count)

#CHALLENGE DONE :D