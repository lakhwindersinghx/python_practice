# CHALLENGE-1:
# my_str = 'wlo1 Link encap:Ethernet HWaddr b4:6d:83:77:85:f3'
# print(my_str[32:]) #s1
# mac=(my_str[-1:31:-1])#s2
# print(mac[::-1])
# mac_list=my_str.split(' ')#s3
# print(mac_list[-1])

#CHALLENGE-2:

# print('It displayed: "You\'ve got an error!\"')
# print('\\n means a new line')
# print('\ is known as the escape character.')

#CHALLENGE-3:
# Write a Python script that converts foot [ft] to centimeter [cm]. 1 ft = 30.48 cm
# The user will be prompted to enter the value in ft.
# Display the value in cm with 2 decimals, formatted using an f-string.
# x=float(input('Enter a number of ft:'))
# print(f'Number of ft: {x} in cm is: {x*30.48}cm')

#CHALLENGE-4: palindrome checker for ex: madam
# x=input("enter your palindrome:")
# for word in x:
#     if x[0::]==x[::-1]:
#         print('It\'s a palindrome')
#     else:
#         print('It\'s not a palindrome')

#CHALLENGE-5: Change the solution of the previous challenge so that both the white spaces
# and the letter case are ignored when checking if the string is a palindrome.

# x=input("enter your palindrome:")
# y=x.lower().strip()
# for word in y:
#     if y[0::]==y[::-1]:
#         print('It\'s a palindrome')
#     else:
#         print('It\'s not a palindrome')

#CHALLENGE-6: Write a Python script to get a string made of the first and the last 2 chars from a given string entered by the user.
# x=input('Enter your sentence:')
# print((x[0:2])+(x[-2:]))

#CHALLENGE-7: Write a Python program to get a string from a given string where all
#occurrences of its first character have been changed to '$', except the first character itself.
#
# my_str=input('enter whatever sentence:')
# n=my_str.replace(my_str[0], '$')
# print(my_str[0]+n[1:])

#CHALLENGE-8: Write a Python program to remove the nth index character from a nonempty string.
# x='shaktimaan is god'
# n=int(input('enter number of index you wanna remove:'))
# print(x[0:n]+(x[n+1:]))

##########################################################################################################

#Second method
# x=list(input('enter your sentence:'))
# str_my=print(''.join(x))
# n=int(input('enter number of index you wanna get rid of bih:'))
# x.pop(n)
# print(''.join(x))

#CHALLENGE-9:Write a Python script that removes the characters which have odd index values of a given string.
# x=input('enter your string:')
# print(x[::2])

#CHALLENGE-10: Write a Python script that prompts the user for
# the radius of a circle and calculates its area. Circle's area = pi * r ** 2 where pi = 3.1415
#
# rad=float(input('enter the radius:'))
# pi=3.1415
# area_circle={f'The area of circle is {pi*rad**2:.4f}'}
# print(area_circle)

#CHALLENGE-11:Write a Python script that finds the number of occurrences
# of a substring in a given string by ignoring the letter case.

# x=input('enter your sentence:').lower()
# print(x.count(input(('enter what you wanna search:'))))

#CHALLENGE-12: Write a Python script that displays a number with a comma
# (,) as the thousands separator (US and UK format)
# and with a period(.) as the thousands separator (EU format).
# n = 12384756982
# n_comma = f'{n:,}'
# print(n_comma)
# print(n_comma.replace(',', '.'))

################################################################################################################
#SOLUTION 2: this is better than solution 1
# x=int(input('enter a number:'))
# x_str=str(x)
# x_comma=''
# count=0
# while count<len(x_str):
#     for number in reversed(x_str):
#         x_comma=number+x_comma
#         count+=1
#         if count%3==0:
#             x_comma=','+x_comma
# print(x_comma)
