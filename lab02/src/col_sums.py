def col_sums(mat):
    kol_simv = len(mat[0])
    for element in mat:
        if len(element)!=kol_simv:
            raise ValueError
    spisok=[0] * kol_simv
    for stroch in mat:
        for stolb in range(len(stroch)):
            spisok[stolb]=spisok[stolb]+stroch[stolb]
    return spisok
mat = [[1, 2, 3], [4, 5, 6]]
print(col_sums(mat))
mat = [[-1, 1], [10, -10]]
print(col_sums(mat))
mat = [[0, 0], [0, 0]]
print(col_sums(mat))
mat = [[1, 2], [3]]
print(col_sums(mat))