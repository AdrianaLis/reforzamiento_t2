print("Comenze") 
def cuenta_regresiva(numero):
    
    if numero <=0:      
        return numero
    print(numero)
    cuenta_regresiva(numero-1)      
cuenta_regresiva(5)
