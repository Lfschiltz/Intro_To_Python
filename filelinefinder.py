import sys

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    sys.exit()
count = 0
for line in fhand:
    count = count + 1
print('There were', count, 'lines in', fname)