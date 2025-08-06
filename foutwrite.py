fout = open('myfile.txt', 'w')
fout.write('My first line of text\n')
fout.write('My second line of text\n')
fout.write('My third line of text\n')
fout.write('My fourth line of text\n')
fout.close()
fin = open('myfile.txt', 'r')

for line in fin:
  print(line)
print()

fin.close()