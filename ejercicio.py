import random
n = int(input("Ingrese el tamaño de la matriz: "))
matriz = []
for i in range(n):
    fila = []
    for j in range(n):
        numero = random.randint(99, 999)
        fila.append(numero)
    matriz.append(fila)
print("\n" + "="*8, "Matriz Generada de:", n, "elementos", "="*8)
for fila in matriz:
    print(" ".join(f"{num:3d}" for num in fila))

def contar_elementoslista(lista):
    if len(lista) == 1:
        numero = lista[0]
        if numero % 5 == 0 or numero % 7 == 0:
            return 1
        else:
            return 0 
    mitad = len(lista) // 2
    izquierda = lista[:mitad]
    derecha = lista[mitad:]
    return contar_elementoslista(izquierda) + contar_elementoslista(derecha)
nueva_lista = []
for fila in matriz:
    nueva_lista.extend(fila)
total = contar_elementoslista(nueva_lista)


print("\n" + "-"*50)
print(f"Cantidad de múltiplos de 5 o 7 encontrados: {total}")
print("-"*50)