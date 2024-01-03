# It returns the number of vowels and consonants in the string as a tuple.
def counter(my_str):
    vowels = 'aeiou'
    vow=tuple()
    conso=tuple()


    # YOUR CODE STARTS HERE
    for letters in my_str:
        if letters in vowels:
            vow+=1
        if letters not in vowels:
            conso+=1
        else:
            vow=1
    print(vow)
counter(my_str='python')



