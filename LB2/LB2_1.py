



def cheker_N():
    while True:

        try:

            argument = int(input())
            if (argument > 0 ):
                break

        except ValueError:
            print('НАСТУПНОГО РАЗУ ВВЕДІТЬ НАТУРАЛЬНЕ  ЧИСЛО:')
            continue
    return argument


def cheker_X():
    while True:

        try:
            argument = float(input())
            break

        except ValueError:
            print('НАСТУПНОГО РАЗУ ВВЕДІТЬ ЧИСЛО:')
            continue

    return argument

def calculate():
    sum = 0
    for i in range(1,n+1):
        sum += (x**i)/(x-n)
    return sum

print("""ЛАБОРАТОРНА РОБОТА №1
ВИКОНАВ СТУДЕНТ 1 КУРСУ ГРУППИ КМ-84
МИСАК ЮРІЙ
ПРОГРАМУВАННЯ ЦИКЛІЧНИХ АЛГОРИТМІВ 
""")

while True:
    print("Введіть: N")
    n = cheker_N()
    print("Введіть: X")
    x = cheker_X()
    if int(x) == n :
        print("N НЕ ПОВИННО = X")
        continue
    print(calculate())