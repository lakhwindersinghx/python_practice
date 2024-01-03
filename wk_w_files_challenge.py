#CHALLENGE 1-Create a new file that contains only unique MAC addresses. Each MAC should be on its own line.
f = open(r"C:\Users\singh\OneDrive\Desktop\Study\python\macs.txt")
content=f.read()


with open('my_file.txt', 'r+') as file:
    file.write('This file will be overwritten!')
    file.write('I am a narcisisti')
    print(file.read())
