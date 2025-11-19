def transpose(mat):
    otvet = []
    if len(mat) == 0:
        return []
    kol_simv = len(mat[0])
    for element in mat:
        if len(element) != kol_simv:
            raise ValueError
    for stolb in range(kol_simv):
        new_stroch = []
        for strochka in range(len(mat)):
            new_stroch.append(mat[strochka][stolb])
        otvet.append(new_stroch)
    return otvet


mat = [[1, 2, 3]]
print(transpose(mat))
mat = [[1], [2], [3]]
print(transpose(mat))
mat = [[1, 2], [3, 4]]
print(transpose(mat))
mat = []
print(transpose(mat))
mat = [[1, 2], [3]]
print(transpose(mat))
