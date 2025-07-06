while True:
    line = input('Enter input (# tag will not print). Type done when finished > ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')