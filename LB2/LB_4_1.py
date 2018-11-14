from math import sqrt


def calculate():
    x =[]
    same=[0, 0, 0, 0]
    x.append((-var[1]+sqrt(((var[1]**2)-4*var[0]*var[2])))/2*var[0])
    x.append((-var[1]-sqrt(((var[1]**2)-4*var[0]*var[2])))/2*var[0])
    x.append((-var[4]+sqrt(((var[4]**2)-4*var[3]*var[5])))/2*var[3])
    x.append((-var[4]-sqrt(((var[4]**2)-4*var[3]*var[5])))/2*var[3])
    for i in range(len(x)-1):
        for j in range(len(x)-1):
            if x[i] == x[j+1]:
                same[i] = 1
                same[j] = 1
    for i in same:
        if i == 0:
            print(x[i])

var = []
print("ДЛЯ ВИВОДУ НАТИСНІТЬ  t(НАСТУПНІ ВВЕДЕНІ КАЄФІЦІЕНТИ БУДУТЬ ВВАЖАТИСЯ )")
print("ВВЕДІТЬ КАЕФІЦІЕНТИ А1,В1,С1,А2,В2,С2 ДЛЯ РІВНЯННЯ ТИПУ АХ^2+BX+C=0")
var_for_exit =''
while var_for_exit != "t":
    var_for_exit = int(input())
    var.append(var_for_exit)
    if len(var) == 6:
        calculate()
        var.clear()


calculate(var)







