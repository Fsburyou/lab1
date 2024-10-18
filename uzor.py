BLUE = '\u001b[44m'
END = '\u001b[0m'

for j in range(7):
    for i in range(6):
        if i % 6 == 0:
            print(f'{END}{" " * 8}{BLUE}{" " * 2}{END}{" " * 12}{BLUE}{" " * 2}{END}{" " * 12}{BLUE}{" " * 2}{END}{" " * 12}{BLUE}{" " * 2}{END}')
        if i % 6 == 3:
            print(f'{END}{" " * 6}{BLUE}{" " * 2}{END}{" " * 2}{BLUE}{" " * 2}{END}{" " * 8}{BLUE}{" " * 2}{END}{" " * 2}{BLUE}{" " * 2}{END}{" " * 8}{BLUE}{" " * 2}{END}{" " * 2}{BLUE}{" " * 2}{END}{" " * 8}{BLUE}{" " * 2}{END}{" " * 2}{BLUE}{" " * 2}{END}')
        if i % 6 == 4:
            print(f'{END}{" " * 4}{BLUE}{" " * 2}{END}{" " * 6}{BLUE}{" " * 2}{END}{" " * 4}{BLUE}{" " * 2}{END}{" " * 6}{BLUE}{" " * 2}{END}{" " * 4}{BLUE}{" " * 2}{END}{" " * 6}{BLUE}{" " * 2}{END}{" " * 4}{BLUE}{" " * 2}{END}{" " * 6}{BLUE}{" " * 2}{END}')
        if i % 6 == 5:
            print(f'{BLUE}{" " * 4}{END}{" " * 10}{BLUE}{" " * 4}{END}{" " * 10}{BLUE}{" " * 4}{END}{" " * 10}{BLUE}{" " * 4}{END}{" " * 10}{BLUE}{" " * 4}{END}')

