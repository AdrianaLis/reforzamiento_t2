def imprime(mat):
    for fil in mat:
        print(fil)
    print()

def sollab(lab, res, x=0, y=0):
    if x == len(lab) - 1 and y == len(lab[0]) - 1:
        if lab[x][y] == 1:
            res[x][y] = 1
            return True
        return False
    if 0 <= x < len(lab) and 0 <= y < len(lab[0]) and lab[x][y] == 1 and res[x][y] == 0:
        res[x][y] = 1
        if sollab(lab, res, x + 1, y):
            return True
        elif sollab(lab, res, x, y + 1):
            return True
        else:
            res[x][y] = 0
            return False
    else:
        return False
lab = [
    [1, 0, 0, 0],
    [1, 1, 1, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]
res = [[0 for _ in range(4)] for _ in range(4)]
if sollab(lab, res):
    print("Salio del lab")
    print("Camino recorrido en la matriz 'res':")
    imprime(res) 
else:
    print("No hay salida")