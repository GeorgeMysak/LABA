


def cheker_N():
    while True:

        try:
            argument = int(input())
            break

        except ValueError:
            print('НАСТУПНОГО РАЗУ ВВЕДІТЬ НАТУРАЛЬНЕ ЧИСЛО:')
            continue

    return argument


def find():
    k = 0
    while 3 * k < N:
        k += 1

    return (k-1)


print("""ЛАБОРАТОРНА РОБОТА №1
ВИКОНАВ СТУДЕНТ 1 КУРСУ ГРУППИ КМ-84
МИСАК ЮРІЙ
ПРОГРАМУВАННЯ ЦИКЛІЧНИХ АЛГОРИТМІВ 
""")



while True:
    print("Введыть N")
    N = cheker_N()
    print(find())