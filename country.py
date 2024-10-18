RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
END = '\u001b[0m'

width = 12

print(f'{RED}{"  " * (width)}{END}')
print(f'{WHITE}{"  " * (width)}{END}')

for i in range(2):
    print(f'{BLUE}{"  " * (width)}{END}')

print(f'{WHITE}{"  " * (width)}{END}')
print(f'{RED}{"  " * (width)}{END}')






