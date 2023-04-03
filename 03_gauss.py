
import numpy as np


def gauss(a,b, n):
    x = np.zeros(n, float)
    for k in range(n - 1):
        if np.fabs(a[k, k]) < 1.0e-12:

            for i in range(k + 1, n):
                if np.fabs(a[i, k]) > np.fabs(a[k, k]):
                    a[[k, i]] = a[[i, k]]
                    b[[k, i]] = b[[i, k]]
                    break

        for i in range(k + 1, n):
            if a[i, k] == 0: continue

            factor = a[k, k] / a[i, k]
            for j in range(k, n):
                a[i, j] = a[k, j] - a[i, j] * factor
            b[i] = b[k] - b[i] * factor

    x[n - 1] = b[n - 1] / a[n - 1, n - 1]
    for i in range(n - 2, -1, -1):
        sum_ax = 0

        for j in range(i + 1, n):
            sum_ax += a[i, j] * x[j]

        x[i] = (b[i] - sum_ax) / a[i, i]

    return x

def extract(list):
    result = []
    for el in list:
        sub = [int(x) for x in el.split(', ')]
        result.append(sub)
    return (result)

if __name__ == '__main__':
    text = open('gauss.txt', 'r')
    list = []
    for x in text:
        list.append(x.strip())
    n1 = list[0]
    b1 = list[1].split()
    b1 = extract(b1)
    b1 = np.array(b1, dtype = float)
    a1= []
    for x in range(2,7):
        a1.append([int(y) for y in list[x].split()])
    a1 = np.array(a1, dtype = float)
    print('Matrix A: ')
    print(a1)


    n2 = list[7]
    b2 = list[8].split()
    b2 = extract(b2)
    b2 = np.array(b2, dtype = float)
    a2 = []
    for x in range(9, 14):
        a2.append([int(y) for y in list[x].split()])
    a2 = np.array(a2, dtype = float)
    print('Matrix B: ')
    print(a2)


    n3 = list[14]
    b3 = list[15].split()
    b3 = extract(b3)
    b3 = np.array(b3, dtype = float)
    a3 = []
    for x in range(16, 21):
        a3.append([int(y) for y in list[x].split()])
    a3 = np.array(a3, dtype = float)
    print('Matrix C: ')
    print(a3)

    text.close()


    print('\n\nMatrix A: ')
    try:
        x = gauss(a1, b1, int(n1))
    except ValueError:
        print("\nMacierz jest źle uwarunkowana lub jedno lub więcej równań w układzie jest liniowo zależnych.")
    else:
        print("\nWynik:", x)
        print("Sprawdzenie A*x: ", np.dot(a1,x))
        
    print('\n\nMatrix B: ')
    try:
        x = gauss(a2, b2, int(n2))
    except ValueError:
        print("\nMacierz jest źle uwarunkowana lub jedno lub więcej równań w układzie jest liniowo zależnych.")
    else:
        print("\nWynik:", x)

    print('\n\nMatrix C: ')
    try:
        x = gauss(a3, b3, int(n3))
    except ValueError:
        print("\nMacierz jest źle uwarunkowana lub jedno lub więcej równań w układzie jest liniowo zależnych.")
    else:
        print("\nWynik:", x)
        print("Sprawdzenie: ", np.round(np.dot(a3, x)))