with open(r'C:\Users\singh\OneDrive\Desktop\Study\python\devices.txt') as my_file:
    content=my_file.read
    ip_list=[]
    for line in content[1:]:
        ip_list.append(line.split(':'))
    print(ip_list)
