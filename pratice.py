import csv

with open('people1.csv', 'w', newline='') as f:
    writer=csv.writer(f, delimiter=':')
    people=[
['Dan', 34, 'Bucharest'],
['Andrei',21, 'London'],
['Maria', 45, 'Paris']
]

    for item in people:
        writer.writerow(item)

with open('people1.csv', 'r') as c:
    reader=csv.reader(c, delimiter=':')
    for row in c:
        print(row)
