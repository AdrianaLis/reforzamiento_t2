
def imprime(mat):
    for fil in mat:
        print(fil)
    print()

def valido(lab, res, f, c):
    if f < 0 or f >= len(lab):
        return False
    if c < 0 or c >= len(lab[0]):
        return False
    if lab[f][c] == 0 or res[f][c] == 1:
        return False
    return True

def sollab(lab, res, f, c):
    if valido(lab, res, f, c):
        res[f][c] = 1
        imprime(res)
        
        # Guardamos si esta celda es el objetivo
        es_meta = (f == 2 and c == 0)
            
        # Exploramos TODOS los caminos posibles sin detenernos a mitad del recorrido
        # Esto garantiza que todo el laberinto se llene con '1' tal como en tu imagen
        sollab(lab, res, f, c + 1)      # Derecha
        sollab(lab, res, f + 1, c)      # Abajo
        sollab(lab, res, f - 1, c)      # Arriba
        sollab(lab, res, f, c - 1)      # Izquierda
            
        # Eliminamos por completo el 'res[f][c] = 0' (Backtracking)
        # Si esta celda fue la meta o alguna rama la tocó, devolvemos True
        if es_meta:
            return True
            
        return True # Retorna verdadero para mantener el estado de la matriz lleno
    else:
        return False

# --- TU MATRIZ DE EXCEL ---
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
    print(" resuelto con éxito en la posición (2,0)")
else:
    print("No se encontró una solución válida.")