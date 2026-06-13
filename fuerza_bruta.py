
contador = 0
def fib_fuerza_bruta(n):
    global contador
    contador += 1    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_fuerza_bruta(n - 1) + fib_fuerza_bruta(n - 2)
n = 5
resultado = fib_fuerza_bruta(n)

print(f"Fibonacci({n}) es: {resultado}")
print(f"La función se llamó {contador} veces.")