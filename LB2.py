import math

def cheker():
    while True:

        try:
            argument = float(input())
            break
        except ValueError:
            print('НАСТУПНОГО РАЗУ ВВЕДІТЬ НАТУРАЛЬНЕ  ЧИСЛО:')
            continue
    return argument


def identifyy(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        if (a ** 2) + (b ** 2) == c ** 2:
            print("Трикутник АВС зі сторонами а: ", a, "b: ", b, "c: ", c, "Э ПРЯМОКУТНИМ")
        else:
            k = ((-(c)**2)+(a**2)+(b**2))/(2*a*b)
            print('КУТ С = ',round(math.degrees(math.acos(k))),' градусів')
    else:
        print("Ваш трикутник не є трикутником, спробуйте ще раз")

print("""ЛАБОРАТОРНА РОБОТА №1
ВИКОНАВ СТУДЕНТ 1 КУРСУ ГРУППИ КМ-84
МИСАК ЮРІЙ
ПРОГРАМУВАННЯ ЛІНІЙНИХ АЛГОРИТМІВ ТА РОЗГАЛУЖЕНИХ ПРОЦЕСІВ
""")

while True:
    print("ВВЕДІТЬ СТОРОНУ a:")
    x = cheker()
    print("ВВЕДІТЬ СТОРОНУ b:")
    y = cheker()
    print("ВВЕДІТЬ СТОРОНУ c:")
    z = cheker()
    identifyy(x, y, z)