
def validarNumero():
    
    while True:
        try:
            numero = int(input("Ingrese una cantidad para la matriz: "))
            break
        except:
            print("Dato no valido.....")
    
    return numero

matriz = []
        
def crearMatriz(cantidad):
    contador = 0
    for i in range(cantidad):
        fila = []
        for j in range(cantidad):
            fila.append(contador)
            contador+=1 
        matriz.append(fila)
            

    for fila in matriz:
        print(fila)
        
cantidadMatriz = validarNumero() 

crearMatriz(cantidadMatriz)






