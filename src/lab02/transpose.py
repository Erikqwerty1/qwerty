def transpose(mat):
    otvet = []
    if len(mat) == 0:
        return []
    kol_simv = len(mat[0])
    for element in mat:
        if len(element)!=kol_simv:
            raise ValueError
    for stolbishe in range(kol_simv):
        new_strochiche = []
        for strochiche in range(len(mat)):
            new_strochiche.append(mat[strochiche][stolbishe])
        otvet.append(new_strochiche)
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