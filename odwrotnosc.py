Am = [[5, 4, 3, 2, 1],
      [4, 3, 2, 1, 5],
      [3, 2, 9, 5, 4],
      [2, 1, 5, 4, 3],
      [1, 2, 3, 4, 5]]
Im = [[1, 0, 0, 0, 0],
      [0, 1, 0, 0, 0],
      [0, 0, 1, 0, 0],
      [0, 0, 0, 1, 0],
      [0, 0, 0, 0, 1]]


def odwrotnosc(A, I):
    Ac = A.copy()
    Ic = I.copy()
    indeksy = list(range(len(A)))
    for i in range(len(Ac[0])):
        dzielnik = Ac[i][i]
        for j in range(len(Ac[0])):
            Ac[i][j] = Ac[i][j]/dzielnik
            Ic[i][j] = Ic[i][j]/dzielnik
        for k in indeksy[0:i] + indeksy[i+1:]:
            skalar = Ac[k][i]
            for m in range(len(A)):
                Ac[k][m] = Ac[k][m] - skalar * Ac[i][j]
                Ic[k][m] = Ic[k][m] - skalar * Ic[i][j]




    return (Ac)

print(odwrotnosc(Am, Im))
