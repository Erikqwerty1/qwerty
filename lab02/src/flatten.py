def flatten(mat):
    otvet = []
    for element in mat:
        if type(element)==tuple or type(element)==list:
            for podelement in element:
                otvet.append(podelement)
        else:
            raise TypeError
    return otvet
mat = [[1, 2], [3, 4]]
print(flatten(mat))
mat = [[1, 2], (3, 4, 5)]
print(flatten(mat))
mat = [[1], [], [2, 3]]
print(flatten(mat))
mat = [[1, 2], "ab"]
print(flatten(mat))
