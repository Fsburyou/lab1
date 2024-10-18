COLOR = '\u001b[44m'
END = '\u001b[0m'

y = ' '
for x in range(30, 1, -1):

    if x % 2 == 0:
        y = int(x / 2) - 1
    if x % 2 != 0 or int(x / 2) == 1:
        y = " "

    print(f'{y}{END}{" " * int((1 / x) * 500 - 12)}{COLOR}{" " * (int((1 / (x - 1)) * 500 - (1 / x) * 500) + 1)}{END}')

step = 100
print(f'{'0'}{END}{" " * step}{'1'}{END}{" " * step}{'2'}{END}{" " * step}{'3'}{END}{" " * step}{'4'}{END}{" " * step}{'5'}')

