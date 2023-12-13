def validarNumero(texto):
    
    while True:
        try:
            numero = int(input(texto))
            break
        except:
            print("Dato no valido.....")
    
    return numero

matriz = []
        
def crearMatriz(fila, columna):
    
    for i in range(fila):
        fila_ = []
        for j in range(columna):
            numero = validarNumero(f"Columna {i+1}: ")
            fila_.append(numero)
        
        matriz.append(fila_)
            

    for x in matriz:
        print(x)
    
    

def sumar_columnas(columna, matriz):
    suma_columnas = [0] * columna
    for i in range(columna):
        suma = 0
        
        for fila in matriz:
            suma+= fila[i]
            
        suma_columnas[i] = suma
    
    print("Suma de cada columna: ")
    print(suma_columnas)
    
    for x in range(columna):
        
        if  suma_columnas[0] != suma_columnas[x]:
            print("La suma de las columnasa no son iguales..")
            break
    else:
        print("La suma de todas las columnas son iguales")
    
fila = validarNumero("Ingrese la cantidad de filas: ") 
columna = validarNumero("Ingrese la cantidad de columnas: ")

crearMatriz(fila, columna)

sumar_columnas(columna, matriz)