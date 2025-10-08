def row_sums(mat):
    kol_simv = len(mat[0])
    for element in mat:
        if len(element)!=kol_simv:
            raise ValueError
    spisok = []
    for element in mat:
        summa=0
        summa = sum(element)
        spisok.append(summa)
    return spisok
mat = [[1, 2, 3], [4, 5, 6]]
print(row_sums(mat))
mat = [[-1, 1], [10, -10]]
print(row_sums(mat))
mat = [[0, 0], [0, 0]]
print(row_sums(mat))
mat = [[1, 2], [3]]
print(row_sums(mat))