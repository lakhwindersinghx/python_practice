#CHALLENGE-1: Create a Python script that removes all the occurrences of a given element of a list.
# s_list=([1,2,3,1,1,1,1,2,3,4,3])
# n_list=[]
# x=int(input('Enter the number you wanna remove: '))
# for n in s_list:
#     if n!=x:
#         n_list.append(n)
# print(n_list)

#SOLUTION-2: USING A WHILE LOOP
# s_list=([1,2,3,1,1,1,1,2,3,4,3])
# x=int(input('Enter the number you want to remove: '))
# while x in s_list:
#     s_list.remove(x)
# print(s_list)

#SOLUTION-3: Making a function
# def rem(s_list,element):
#     while element in s_list:
#         s_list.remove(element)
#     print(s_list)
#     return(s_list)
# rem(s_list=[1,2,3,1,1,1,1,2,3,4,3],element=1)

#SOLUTON-4: USING OOP concept-
# class removal:
#     def __init__(self,s_list,element):
#         self.s_list=s_list
#         self.element=element
#         while element in s_list:
#             s_list.remove(element)
#         print(s_list)
# x=removal(s_list=[1,2,3,1,1,1,1,2,3,4,3],element=1)

# #CHALLENGE-2: Create a Python script that removes all the elements of a list that are duplicates.
# I am trying to use OOP concepts and most likely be using the same syntax in further solutions
# class dupli():
#     def __init__(self,s_list,n_list):
#         self.sample=s_list
#         self.new=n_list
#         for item in s_list:
#             if item not in n_list:
#                 n_list.append(item)
#         print(n_list)
# result=dupli(s_list=[1,2,3,1,1,1,1,2,3,4,3],n_list=[])

#CHALLENGE 3-Consider the following string: nums = '10,20,30,40,50'
#Create a Python script that creates a list of integers from the string

# class slist():
#     def __init__(self,nums):
#         self.nums=nums
#         print(nums.split())
#
# result=slist(nums='10,20,30,40,50')

#CHALLENGE 4- Write a Python script that finds all numbers that are
# divisible by 7 but are not a multiple of 5, between 1500 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence (CSV) on a single line.
# class multipl():
#     def __init__(self,nlist):
#         self.nlist=nlist
#         for item in range(1500,3201):
#             if item%7==0 and item%5!=0:
#                 nlist.append(item)
#         print(nlist)
# result=multipl(nlist=[])

#CHALLENGE 6- Write a program that prompts the user for a long string containing multiple words
#separated by whitespaces and prints back the same string with the words in backward order.
#For example, say I type the string: My name is Andrei
#Then the script should print out: Andrei is name My

# class rev():
#     def __init__(self,my_str):
#         self.my_str=my_str
#         print(my_str)
#         words=my_str.split(' ')
#         print(words)
#         print(' '.join(reversed(words)))
# result=rev(my_str='My name is Andrei')

#CHALLENGE-6:Write a Python program that accepts a hyphen-separated sequence of words as input
# and prints the words in a hyphen-separated sequence after sorting them alphabetically.
#Sample input string : green-red-yellow-black-whitE
#Expected Result : black-green-red-white-yelloW

# class Sortx():
#     def __init__(self,sample):
#         self.sample=sample
#         print(sample)
#         sample_list=sample.split('-')
#         reverse_list='-'.join(sorted(sample_list))
#         print(reverse_list)
# result=Sortx(sample='green-red-yellow-black-white')

#CHALLENGE-7:
# Write a Python program that accepts as input a sequence of words separated by one or more whitespaces
# and prints out the same words with the letters in reversed order. Do not use list comprehension.
# Sample input string: I love cat and dogs
# Expected Result: I evol tac dna sgod


# string = input("Enter a few words separated by whitespaces: ")
# words = string.split()
# # reverse the letters in each word
# i = 0
# for w in words:
#     words[i] = w[::-1]
#     i += 1
# new_str = ' '.join(words)
# print(new_str)

#CHALLENGE-9: Create a Python script that calculates and displays the number of occurrences of each element of a list.
#Sample list: list('mamma mia mm')
# #Expected Result:
# m ---> 6
# a ---> 3
# ---> 2
# i ---> 1
# class Numb():
#     def __init__(self,sample):
#         self.sample=sample
#         sample_list=list(sample)
#         x=[]
#         for item in sample_list:
#             y=sample_list.count(item)
#             if y not in x:
#                 x.append(y)
#         print(x)
# result=Numb(sample='mamma mia mm')
#THIS IS AN INCOMPLETE SOLUTION

#FOUND THIS SOLTUION ON CHATGPT AND ITS GOOD:

# class Numb():
#     def __init__(self,sample):
#         self.sample=sample
#         occurrence={}
#         sample_list=list(sample)
#         for item in sample_list:
#             if item in occurrence:
#                 occurrence[item]+=1
#             else:
#                 occurrence[item]=1
#         for item, count in occurrence.items():
#             print(f"Element '{item}' occurs {count} times.")
# result=Numb('mamma mia mm')

#CHALLENGE-10:# Consider a list of words(strings). Write a Python script
# # that generates a list of tuples where the first element of the tuple is the word in the list and the second element is its length.
# # # Use list comprehension if possible.
# Sample List: words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']
#
# words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']
# x=[]
# for item in words:
#     x.append((item,len(item)))
# print(x)

