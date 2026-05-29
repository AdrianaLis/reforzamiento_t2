def sumar_elementos(lstnumero,total_elementos):
  
    if len(lstnumero)==1:
      return lstnumero[0]/total_elementos
    
    primer_numero=lstnumero[0]/total_elementos
    resto_lista=lstnumero[1:]
    return primer_numero+sumar_elementos(resto_lista,total_elementos)
    
  
mis_notas = [10, 20, 5, 2, 3]
total = len(mis_notas)


resultado = sumar_elementos(mis_notas, total)
print("El promedio es:", resultado)  
    

    
     
    