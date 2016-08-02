import csv
import os

def read_secrets():
    print 'IN READ SECRETS PATH = ', os.path.abspath('.')
    with open('secrets//example_secrets.txt') as s:
        secret_reader = csv.reader(s)
        for row in secret_reader:
            a, b, c, d = [r for r in row]
    return a, b, c, d

if __name__ == '__main__':
    print 'In main'
    a, b, c, d = read_secrets()
    print 'a,b,c,d = ', a, b, c, d

