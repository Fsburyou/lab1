COLOR = '\u001b[44m'
END = '\u001b[0m'

f = open("sequence.txt")
n = 250

big = 0
mid = 0
small = 0

for i in range(n):
    s = f.readline()
    s1 = ''
    s2 = s1
    mn = 0
    d = 0
    for j in s:
        if j in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if d == 0:
                s1 += j
            if d == 1:
                s2 += j
        if j == '-':
            mn = 1
        if j == '.':
            d = 1
    num = int(s1)
    if int(s2) != 0:
        num += int(s2) ** ((-10) * len(s2))
    if mn == 1:
        num *= -1
    if num >= 0:
        if num > 5:
            big += 1
        if num < 5:
            small += 1
        if num == 5:
            mid += 1

up = max(big, small) + 5

for i in range(up, min(big, small) - 10, -1):
    if i <= small:
        if i <= big:
            print(f'{COLOR}{" " * 3}{END}{" " * 1}{COLOR}{" " * 3}{END}')
        else:
            print(f'{COLOR}{" " * 3}{END}')
    else:
        print(f'{END}')

