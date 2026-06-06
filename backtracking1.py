def imprime(mat):
    for fil in mat:
        print(fil)
    print()

def valido(lab, f, c):
    if f >= len(lab):
        return False
    if c >= len(lab[0]):
        return False
    if lab[f][c] == 0:
        return False
    return True
   

def sollab(lab, res, f, c):
    if f == len(lab)-1 and c == len(lab[0])-1:
        if lab[f][c] == 1:
            res[f][c] = 1
            imprime(res)
            return True
        else:
            return False
    else:
        if valido(lab, f, c):
            res[f][c] = 1
            imprime(res)
            if sollab(lab, res, f, c+1):
                return True
            elif sollab(lab, res, f+1, c):
                return True
            else:
                res[f][c] = 0
                return False
        else:
            return False
        
lab = [
    [1,0,0,0],
    [1,1,1,1],
    [0,1,0,0],
    [1,1,1,1]
]
res = [[0 for _ in range(4)] for _ in range(4)]

if sollab(lab, res, 0, 0):
    print("Salio del lab")
else:
    print("No hay aslida")