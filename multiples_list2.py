multiples = []
for threeD in range(1,3):
 multiples.append([])
 for twoD in range(1,3):
  multiples[threeD-1].append([])
  for oneD in range(1,3):
   multiples[threeD-1][twoD-1].append(oneD)
print(multiples)