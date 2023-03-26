"""
1 Obliczanie wartości wielomianu zadanego w postaci naturalnej
dla dowolnej wartości x z wykorzystaniem schematu Hornera

2 Obliczanie wartości wielomianu zadanego w postaci Newtona
dla dowolnej wartości x z wykorzystaniem uogólnionego
schematu Hornera

3 Przekształcenie wielomianu z postaci Newtona na postać
naturalną (przeliczenie współczynników)

4 Interpolacja Lagrange’a

Implementacja numeryczna (preferowany język programowania
C++)

Testowanie poprawności działania algorytmu

5 Postać Newtona wielomianu Lagrange’a - wyznaczanie
ilorazów różnicowych"""

import numpy as np

def interpolacja(xx, yy, x, y):
    for i in range(n+1):
        w=1
        for j in range(n+1):
            if j != i:
                w = w*(x - xx[j])/(xx[i] - xx[j])
        y = y+yy[i]*w
    print('y=', y)

text = open('interpolacja_gr_3.txt', 'r')
list =[]
for x in text:
    list.append(x.strip())
xx = list[0].split()
yy = list[1].split()
print(xx)
print(yy)
xx = np.array(xx, float)
yy = np.array(yy, float)
m = len(xx)
n = m-1
x = float(input('x= '))
y = 0
interpolacja(xx, yy, x,y)
text.close()

