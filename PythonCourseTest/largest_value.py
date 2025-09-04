largestValue = None
print('Before:', largestValue)
for itervar in [3, 41, 12, 9, 74, 15]:
    if largestValue is None or itervar > largestValue:
        largestValue = itervar
    print('Loop:', itervar, largestValue)
print('Largest:', largestValue)