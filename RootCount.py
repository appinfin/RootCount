
Af = True
Bf = True
Cf = True

def root_count(A, B, C):
    """ Вычисляет число корней квадратного ур-ния
    """
    if A!=0:
        D = B**2 - 4*A*C
        if D > 0:
            print(f'D = {round(D, 2)} -> Два корня: ', end=' ')
            print(f'X1 = {round((-B -D**0.5) / (2*A), 2)};', end=' ')
            print(f'X2 = {round((-B +D**0.5) / (2*A), 2)}')
        elif D == 0:
            print(f'D = {round(D, 2)} -> Один корень', end=' ')
            print(f'X = {round(-B / (2*A), 2)}')
        else:
            print(f'D = {round(D, 2)} -> Корней нет')
    else:
        print(f'Ур-ние с коэффициентом А = 0 не является квадратным')

for i in range(1,6): # кол-во уравнений от 1 до 6 (5 шт.)
    while Af:
        try:
            A = float(input('Введите коэффициент А = '))
            Af = False
        except Exception:
            pass
    while Bf:
        try:
            B = float(input('Введите коэффициент B = '))
            Bf = False
        except Exception:
            pass
    while Cf:
        try:
            C = float(input('Введите коэффициент C = '))
            Cf = False
        except Exception:
            pass
    print(f'Уравнение № {i}')
    root_count(A, B, C)
    Af = True
    Bf = True
    Cf = True
