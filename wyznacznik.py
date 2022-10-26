import numpy as np
#Mateusz Gorzynski lab 1

def wyznacznik_macierzy(A):
    wynik = 0
    indeksy = list(range(len(A)))

    if (len(A[0]) == 2 and len(A) == 2):
        return A[0][0] * A[1][1] - A[1][0] * A[0][1]
    else:
        for ind in indeksy:
            Ac = A.copy()
            Ac = Ac[1:len(A)]

            height = len(Ac)

            for i in range(height):
                Ac[i] = np.delete(Ac[i], ind)

            znak = (-1) ** (ind % 2)

            podmacierz = wyznacznik_macierzy(Ac)
            wynik += znak * podmacierz * A[0][ind]

    return wynik


matrix1 = [[2, 4],
           [1, 3]]
matrix2 = [[1, 9, 6],
           [7, 66, 1],
           [3, 2, 2]]

print(wyznacznik_macierzy(matrix2))
print(np.linalg.det(matrix2))