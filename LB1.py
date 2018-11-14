def calСulate(x):
    return x**5 + abs(x)

print("""ЛАБОРАТОРНА РОБОТА №1
ВИКОНАВ СТУДЕНТ 1 КУРСУ ГРУППИ КМ-84
МИСАК ЮРІЙ
ПРОГРАМУВАННЯ ЛІНІЙНИХ АЛГОРИТМІВ ТА РОЗГАЛУЖЕНИХ ПРОЦЕСІВ
""")

while True :

    argument = input("ВВЕДІТЬ ЦІЛЕ ЧИСЛО:")
    try:
        argument = int(argument)
    except ValueError:
        print('НАСТУПНОГО РАЗУ ВВЕДІТЬ ЦІЛЕ ЧИСЛО:')
        continue

    print(calСulate(int(argument)))
