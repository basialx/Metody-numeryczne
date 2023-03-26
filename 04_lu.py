import numpy as np

def lu_decomposition(A):
    n = A.shape[0]
    U = A.copy()
    L = np.eye(n, dtype=np.double)
    for i in range(n):
        factor = U[i + 1:, i] / U[i, i]
        L[i + 1:, i] = factor
        U[i + 1:] -= factor[:, np.newaxis] * U[i]
    return L, U

def extract(list):
    result = []
    for el in list:
        sub = [int(x) for x in el.split(', ')]
        result.append(sub)
    return (result)

def multiply_matrix(A,B, rows, cols):
  global C
  if  A.shape[1] == B.shape[0]:
    C = np.zeros((A.shape[0],B.shape[1]),dtype = int)
    for row in range(rows):
        for col in range(cols):
            for elt in range(len(B)):
              C[row, col] += A[row, elt] * B[elt, col]
    return C
  else:
    return "Sorry, cannot multiply A and B."

def lu_solve(a, b, l, u):
    # Rozwiązanie Lz = b
    z = np.zeros_like(b)
    n = len(a)
    for i in range(n):
        z[i] = b[i]
        for j in range(i):
            z[i] -= l[i, j] * z[j]
        z[i] /= l[i, i]

    # Rozwiązanie Ux = z
    x = np.zeros_like(b)
    for i in range(n - 1, -1, -1):
        x[i] = z[i]
        for j in range(i + 1, n):
            x[i] -= u[i, j] * x[j]
        x[i] /= u[i, i]

    return x

if __name__ == '__main__':
    text = open('LU_gr3.txt', 'r')
    list = []
    for x in text:
        list.append(x.strip())
    n = list[0]
    b = list[1].split()
    b = extract(b)
    b = np.array(b, dtype=float)
    a = []
    for x in range(2, 7):
        a.append([int(y) for y in list[x].split()])
    a = np.array(a, dtype=float)
    print('Matrix A: ')
    print(a)
    L, U = lu_decomposition(a)
    print('L = ')
    print(L)
    print('U = ')
    print(U)
    print('L*U = ')
    print(multiply_matrix(L,U, 5,5))
    print('Rozwiązanie x: ')
    x = lu_solve(a,b,L, U)
    print(x)
    print('Sprawdzenie poprawności: ')
    print('A*x = ')
    s = multiply_matrix(a,x, 5, 1)
    print(s)
    print('')
    print('A*x z wykorzystaniem numpy:')
    print(np.matmul(a,x))
    print('b = ')
    print(b)
    print("Wyniki są zgodne.")