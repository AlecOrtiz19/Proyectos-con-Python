from collections import deque

def validarNumero():
    
    while True:
        try:
            numero = int(input("Ingrese un numero a la cola: "))
            break
        except:
            print("Dato no valido.....")
    
    return numero

def cola():
    cola = deque()
    total = 0
    cantidad = 0
    
    while True:
        dato_ingresado = validarNumero()
        
        if dato_ingresado == 0:
            print("terminado...")
            break
        
        cola.append(dato_ingresado)
        total+=dato_ingresado
        cantidad +=1
        
    if len(cola) == 0:
        print("No se ingresaron datos...")
        
    else:
        print("---Elementos en su orden de salida--- \n")

        while cola:
            elemento = cola.popleft()
            print(elemento)
        
        promedio = total / cantidad
        
        print(f"El promedio de la cola es: {promedio} ")
        
cola()







