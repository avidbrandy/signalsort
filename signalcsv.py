from datetime import datetime
import csv
import os

file = open('messages.csv', 'r')
reader = csv.reader(file)
columns = next(reader)

n_contacts = 0
for c, line in enumerate(reader):
    conversation = line[7]
    if not os.path.isfile(f'{conversation}.csv'):
        with open(f'{conversation}.csv', 'w') as contact:
            writer = csv.writer(contact, delimiter=',')
            writer.writerow(columns)
        n_contacts += 1
        if n_contacts % 10 == 0:
            print(f'{n_contacts} files created...')
print(f'{n_contacts} files created. adding messages to files...')

del(file)
file = open('messages.csv', 'r')
reader = csv.reader(file)
columns = next(reader)


for i, line in enumerate(reader):

    line[5] = str(datetime.fromtimestamp(int(str(line[5])[0:10])))
    line[8] = str(datetime.fromtimestamp(int(str(line[8])[0:10])))

    conversation = line[7]
    with open(f'{conversation}.csv', 'a') as contact:
        writer = csv.writer(contact, delimiter=',')
        writer.writerow(line)
    if i % 1000 == 0:
        print(f'{i} of {c} messages sorted...')
print('And it\'s done!')
