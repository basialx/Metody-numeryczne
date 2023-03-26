import time
import numpy as np

def horner(a, x):
    #schemat Hornera
    n = len(a)
    result = a[0]
    for i in range(1, n):
        result = result * x + a[i]
    return result

def polynomial(a, x):
    #postac naturalna
    result = a[0]
    for i in range(1, len(a)):
        result = result * x + a[i]
    return result

def newton(xx, yy):
    #współczynniki w postaci Newtona
    n = len(xx)
    a = yy.copy()
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            a[i] = (a[i] - a[i-1]) / (xx[i] - yy[i-j])
    return a

def newton_interpolation(xx, yy, x):
    #wartość wielomianu interpolacyjnego w postaci Newtona dla podanych punktów (x,y) i wartości x.
    a = newton(xx, yy)
    n = len(xx)
    result = a[n-1]
    for i in range(n-2, -1, -1):
        result = result * (x - xx[i]) + a[i]
    return result

if __name__ == '__main__':
    text = open('interpolacja_H_gr_3.txt', 'r')
    list = []
    for x in text:
        list.append(x.strip())
    aa = list[0].split()
    xx = list[1].split()
    print(aa)
    print(xx)
    aa = np.array(aa, float)
    xx = np.array(xx, float)

    start_time = time.time()
    for x in xx:
        polynomial(aa, x)
    end_time = time.time()
    time1 = end_time - start_time
    start_time = time.time()
    for x in xx:
        horner(aa, x)
    end_time = time.time()
    time2 = end_time - start_time

    print("Czas wykonania funkcji 1:", time1)
    print("Czas wykonania funkcji 2:", time2)

    text.close()

    text = open('interpolacja_N_gr_3.txt', 'r')
    list = []
    for x in text:
        list.append(x.strip())
    xx = list[0].split()
    yy = list[1].split()
    print(xx)
    print(yy)
    xx = np.array(xx, float)
    yy = np.array(yy, float)

    a = newton(xx, yy)
    print("Współczynniki w postaci Newtona:")
    print(a)
    x = float(input("Podaj wartość x: "))
    result = newton_interpolation(xx, yy, x)
    print("y = ", result)
    text.close()

