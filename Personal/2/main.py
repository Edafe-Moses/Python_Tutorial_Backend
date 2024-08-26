a = open('./countries.txt', 'r')
# print(a.readlines()[0])
for lines in a.readlines():
    print(lines, end='')
a.close()