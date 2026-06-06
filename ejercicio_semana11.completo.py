def imprime(mat):
    for fil in mat:
        print(fil)
    print()

def valido(lab, res, f, c):
    # Controla que no se salga de los bordes (arriba, abajo, izquierda, derecha)
    if f < 0 or f >= len(lab):
        return False
    if c < 0 or c >= len(lab[0]):
        return False
    # Controla que no choque con pared (0) ni pase por donde ya caminó (1)
    if lab[f][c] == 0 or res[f][c] == 1:
        return False
    return True

def sollab(lab, res, f, c):
    if valido(lab, res, f, c):
        # Registro avance: marcamos e imprimimos el paso actual
        res[f][c] = 1
        imprime(res)
        
        # ---- CASO BASE DINÁMICO (Llegar al final de la matriz) ----
        if f == len(lab) - 1 and c == len(lab[0]) - 1:
            return True
            
        # ---- MOVIMIENTOS RECURSIVOS ----
        if sollab(lab, res, f, c + 1):      # 1. Intentar DERECHA
            return True
        elif sollab(lab, res, f + 1, c):    # 2. Intentar ABAJO
            return True
        elif sollab(lab, res, f - 1, c):    # 3. Intentar ARRIBA
            return True
        elif sollab(lab, res, f, c - 1):    # 4. Intentar IZQUIERDA
            return True
            
        # ---- BACKTRACKING (Si fallan todos los movimientos) ----
        res[f][c] = 0
        return False
    else:
        return False
laberinto = [
    [1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 0],
    [1, 1, 0, 1, 1, 1, 1, 0, 1], 
    [0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1]
]
resultado = [[0] * len(laberinto[0]) for _ in range(len(laberinto))]

if sollab(laberinto, resultado, 0, 0):
    print("¡Laberinto resuelto con éxito en la esquina inferior derecha!")
else:
    print("No se encontró una solución válida.")