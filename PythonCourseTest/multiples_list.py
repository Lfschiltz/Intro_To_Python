multiples = []
for outer in range(1,11):
  multiples.append([])
  for inner in range(1,11):
    multiples[outer-1].append( outer * inner)
print(multiples)

for outerList in multiples:
  for innerValue in outerList:
    print (innerValue," ",end ='')
  print()