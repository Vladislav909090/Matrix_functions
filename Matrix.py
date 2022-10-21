import random


def m_show(mas):
    print("[", end="")
    for i in range(len(mas)):
        if i == len(mas) - 1:
            print(mas[i], end="")
            print("]")
        else:
            print(mas[i])


def m_create(n, k):
    mas = []
    for i in range(n):
        mas.append([None] * k)
    return mas


def m_sum(mas1, mas2):
    n1, k1 = len(mas1), len(mas1[0])
    n2, k2 = len(mas2), len(mas2[0])
    if n1 == n2 and k1 == k2:
        mas3 = m_create(n1, k1)
        for i in range(n1):
            for j in range(k1):
                mas3[i][j] = mas1[i][j] + mas2[i][j]
        return mas3
    else:
        print("Error: these matrices cannot be folded")
        raise SystemExit


def m_multiplnum(mas1, num):
    n, k = len(mas1), len(mas1[0])
    mas2 = m_create(n, k)
    for i in range(n):
        for j in range(k):
            mas2[i][j] = mas1[i][j] * num
    return mas2


def m_transp(mas1):
    n, k = len(mas1), len(mas1[0])
    mas2 = m_create(n, k)
    for i in range(n):
        for j in range(k):
            mas2[j][i] = mas1[i][j]
    return mas2


def m_multipl(mas1, mas2):
    n1, k1 = len(mas1), len(mas1[0])
    n2, k2 = len(mas2), len(mas2[0])
    if k1 == n2:
        mas3 = m_create(n1, k2)
        for i in range(n1):
            for j in range(k2):
                mas3[i][j] = sum([mas1[i][l] * mas2[l][j] for l in range(0, k1)])
        return mas3
    else:
        print("Error: these matrices cannot be multiplied")
        raise SystemExit


def m_input(mas1, mas2):
    n, k = [int(i) for i in mas1.split()]
    mas2 = [int(i) for i in mas2.split()]
    r = 0
    mas3 = m_create(n, k)
    for i in range(n):
        for j in range(k):
            mas3[i][j] = mas2[r]
            r += 1
    return mas3


# m_input() - запись матрицы в виде:
# 2 2
# 3 4 5 6

def m_determ(mas):
    n, k = len(mas), len(mas[0])
    if n == k:
        if n == 1:
            return mas[0][0]
        if n == 2:
            return mas[0][0] * mas[1][1] - mas[0][1] * mas[1][0]
        else:
            s = 0
            for i in range(n):
                r = []
                for a in range(1, n):
                    l = []
                    for b in range(n):
                        if b != i:
                            l += [mas[a][b]]
                    if l != []:
                        r += [tuple(l)]
                s += m_determ(tuple(r)) * mas[0][i] * (-1) ** i
            if s == 0:
                print("Error: the determinant of the matrix is zero")
                raise SystemExit
            else:
                return s
    else:
        print("Error: impossible to find a determinant for this matrix")


def m_algebr_complement(i, j, mas):
    n, k = len(mas), len(mas[0])
    if n == k:
        return m_determ(mas) * (-1) ** (i + j)
    else:
        print("Error: impossible to find a determinant for algebraic complement")
        raise SystemExit


def m_algebr_add(mas):
    n, k = len(mas), len(mas[0])
    if n == k:
        mas1 = m_create(n, k)
        for i in range(n):
            for j in range(n):
                r = []
                for a in range(n):
                    l = []
                    for b in range(n):
                        if a != i and b != j:
                            l += [mas[a][b]]
                    if l != []:
                        r += [l]
                mas1[i][j] = m_algebr_complement(i, j, r)
        return mas1
    else:
        print("Error: impossible to find the matrix of algebraic complements")
        raise SystemExit


def m_inverse(mas):
    n, k = len(mas), len(mas[0])
    return m_transp(m_multiplnum(mas, 1 / m_determ(mas)))


def m_power(mas, stepen):
    n, k = len(mas), len(mas[0])
    mas2 = mas
    if n == k:
        if stepen == 1:
            for i in range(n):
                for j in range(n):
                    if i == j:
                        mas2[i][j] = 1
                    else:
                        mas2[i][j] = 0
        else:
            for i in range(stepen - 1):
                mas2 = m_multipl(mas2, mas)
        return mas2
    else:
        print("Error: the matrix cannot be raised to a power")
        raise SystemExit


def m_random(n, k, bottom=-10, top=10):
    mas = m_create(n, k)
    for i in range(n):
        for j in range(k):
            mas[i][j] = (random.randint(bottom, top))
    return mas


# Все функции с матрицами:
# m_show(mas)                        --> красивый вывод матрицы
# m_create(n, k)                     --> создание матрицы размером n на k
# m_sum(mas1, mas2)                  --> сумма матриц
# m_multiplnum(mas1, num)            --> умножение матрицу на число
# m_transp(mas1)                     --> транспонирование матрицу
# m_multipl(mas1, mas2)              --> умножение матрицу на матрицу
# m_input(mas1, mas2)                --> ввод матрицу в виде "сначала в строке размер потом в след строке числа
# m_determ(mas)                      --> определитель матрицы
# m_algebr_complement(i, j, mas)     --> алгебраическое дополнение числа из матрицы позиции i, j
# m_algebr_add(mas)                  --> матрица алгебраических дополнений
# m_inverse(mas)                     --> обратная матрица
# m_power(mas, stepen)               --> возведение матрицы в степень
# m_random(n, k, bottom=-10, top=10) --> матрица размером n на k со случайными значениями в диапазоне

# A = m_input(input(), input())
# B = m_input(input(), input())
# C = m_input(input(), input())
# num = int(input())
#
# m_show(m_multipl(A, m_sum(m_multiplnum(B, num), m_transp(C))))

print(m_determ(m_random(100, 11, 10, 1)))
