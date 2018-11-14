import math

def cheker():
    argument = input()
    try:
        argument = int(argument)
    except ValueError:
        print('НАСТУПНОГО РАЗУ ВВЕДІТЬ ЦІЛЕ  ЧИСЛО:')
    return int(argument)

def MY_Function(a):
    if a > -4:
        return print(math.cos(2*a) + 9)
    else:
        return print((-(math.cos(a)/(a-9))))


print("""ЛАБОРАТОРНА РОБОТА №1
ВИКОНАВ СТУДЕНТ 1 КУРСУ ГРУППИ КМ-84
МИСАК ЮРІЙ
ПРОГРАМУВАННЯ ЛІНІЙНИХ АЛГОРИТМІВ ТА РОЗГАЛУЖЕНИХ ПРОЦЕСІВ
""")

while True:
    print('ВВЕДІТЬ Х ДЛЯ F(X) : ')
    x = cheker()

    MY_Function(x)