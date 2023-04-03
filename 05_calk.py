import numpy as np
import math

def extract(list):
    result = []
    for el in list:
        sub = [int(x) for x in el.split(', ')]
        result.append(sub)
    return (result)

def horner(a, x):
    #schemat Hornera
    n = len(a)
    result = a[0]
    for i in range(1, n):
        result = result * x + a[i]
    return result

def trapezoidal_rule(a, b, n, a_coeffs):
    a_coeffs = np.flip(a_coeffs)
    h = (b-a) / n
    integration = horner(a_coeffs, a) + horner(a_coeffs, b)
    for i in range(1, n):
        k = a + i * h
        integration = integration + 2 * horner(a_coeffs, k)
    integration = integration * h / 2
    return integration


def simpsons_rule(a, b, n, a_coeffs):
    h = (b - a) / n
    a_coeffs = np.flip(a_coeffs)
    integration = horner(a_coeffs, a) + horner(a_coeffs, b)
    for i in range(1, n):
        k = a + i * h
        if i % 2 == 0:
            integration = integration + 2 * horner(a_coeffs, k)
        else:
            integration = integration + 4 * horner(a_coeffs, k)
    integration = integration * h / 3

    return integration


def trapezoidal_rule2(a, b, n, f):
    h = (b-a) / n
    integration = f( a) + f(b)
    for i in range(1, n):
        k = a + i * h
        integration = integration + 2 * f( k)
    integration = integration * h / 2
    return integration


def simpsons_rule2(a, b, n, f):
    h = (b - a) / n
    integration = f( a) + f( b)
    for i in range(1, n):
        k = a + i * h
        if i % 2 == 0:
            integration = integration + 2 * f(k)
        else:
            integration = integration + 4 * f(k)
    integration = integration * h / 3

    return integration
if __name__ == '__main__':
    text = open('kwadratury_gr_3.txt', 'r')
    list = []
    for x in text:
        list.append(x.strip())
    n = int(list[0])
    a = list[1].split() #wspolczynniki
    a = extract(a)
    a = np.array(a, dtype=float)
    ab = list[2].split()
    ab = extract(ab)
    ab = np.array(ab, dtype=float)
    print('Wartość całki za pomocą wzoru trapezów:')
    print(trapezoidal_rule( ab[0], ab[1], 10000, a))
    print('Wartość całki za pomocą wzoru Simpsona:')
    print(simpsons_rule(ab[0], ab[1], 10000, a))
    f = lambda x: x**2 * (math.cos(x))**3
    print('\n')
    print('Dla funkcji f(x) = x^2 * (cos(x))^3:')
    aa = 2
    bb= 6

    print('Wartość całki za pomocą wzoru trapezów:')
    print(trapezoidal_rule2(aa, bb, 10000, f))
    print('Wartość całki za pomocą wzoru Simpsona:')
    print(simpsons_rule2(aa, bb, 10000, f))
    print('Podaj n dla funkcji f(x) = x^2 * (cos(x))^3: ')
    print(input(n))
    for n in range(n, 10000, n**2):
        print('\n')
        print('Wartość całki za pomocą wzoru trapezów:')
        print(trapezoidal_rule2( aa, bb, n, f))
        print('Wartość całki za pomocą wzoru Simpsona:')
        print(simpsons_rule2(aa, bb, n, f))


    print('Podaj n fla funkcji wielomianowej: ')
    print(input(n))
    for n in range(n, 10000, n**2):
        print('Wartość całki za pomocą wzoru trapezów:')
        print(trapezoidal_rule( ab[0], ab[1], n, a))
        print('Wartość całki za pomocą wzoru Simpsona:')
        print(simpsons_rule(ab[0], ab[1], n, a))
