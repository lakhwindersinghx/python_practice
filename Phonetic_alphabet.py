alphabet=dict()
with open(r'C:\Users\singh\OneDrive\Desktop\Study\python\phonetic_alphabet.csv') as f:
    content= f.read().splitlines()
    #print(content)
    for item in content[1:]:
        letter, word=item.split(',')
        alphabet[letter]=word
    print(alphabet)

testing=input('enter:').upper().strip()
for item in testing:
    print(alphabet[item],end='   ')

