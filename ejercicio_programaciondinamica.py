contador = 0

def formasEscalera(n):
    # Paso 1: Crea tu "bloc de notas" (lista con -1)
    memo = [-1 for _ in range(n + 1)]
    return resolver(n, memo)

def resolver(n, memo):
    global contador
    contador += 1
    
    # Paso 2: Casos base
    if n == 0: return 1
    if n < 0: return 0
    
    # Paso 3: ¿Ya lo calculé antes?
    if memo[n] != -1:
        return memo[n]
    
    # Paso 4: Si no, lo calculo (1, 2 o 3 pasos) y lo guardo
    memo[n] = resolver(n - 1, memo) + resolver(n - 2, memo) + resolver(n - 3, memo)
    return memo[n]

# Prueba con 10 escalones
n = 10
resultado = formasEscalera(n)
print(f"Formas de subir {n} escalones: {resultado}")
print(f"Número de llamadas realizadas: {contador}")