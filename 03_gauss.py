import sys
import numpy as np

def gauss_elimination(A, b, n):
    n = A.shape[0]
    Ab = np.concatenate((A, b.reshape(n, 1)), axis=1, dtype=float)
    for i in range(n):
        # Częściowe pivoting
        max_row = i
        for j in range(i + 1, n):
            if abs(Ab[j, i]) > abs(Ab[max_row, i]):
                max_row = j
        Ab[[i, max_row]] = Ab[[max_row, i]]
        # Eliminacja Gaussa
        if Ab[i, i] == 0:
            raise ValueError("Macierz jest źle uwarunkowana lub jedno z równań jest liniowo zależne.")
        for j in range(i + 1, n):
            if Ab[j, i] == 0:
                continue
            factor = Ab[j, i] / Ab[i, i]
            Ab[j, :] -= factor * Ab[i, :]
    # Wyliczenie wektora niewiadomych
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        if Ab[i, i] == 0:
            raise ValueError("Macierz jest źle uwarunkowana lub jedno z równań jest liniowo zależne.")
        x[i] = (Ab[i, n] - np.dot(Ab[i, :i], x[:i])) / Ab[i, i]
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


    print('Matrix A: ')
    try:
        x = gauss_elimination(a1, b1, int(n1))
    except ValueError:
        print("Macierz jest źle uwarunkowana lub jedno lub więcej równań w układzie jest liniowo zależnych.")
    else:
        print("Wynik:", x)



    print('Matrix B: ')
    try:
        x = gauss_elimination(a2, b2, int(n2))
    except ValueError:
        print("Macierz jest źle uwarunkowana lub jedno lub więcej równań w układzie jest liniowo zależnych.")
    else:
        print("Wynik:", x)



    print('Matrix C: ')
    try:
        x = gauss_elimination(a3, b3, int(n3))
    except ValueError:
        print("Macierz jest źle uwarunkowana lub jedno lub więcej równań w układzie jest liniowo zależnych.")
    else:
        print("Wynik:", x)