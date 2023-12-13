

def validarNumero(texto):
    
    while True:
        try:
            numero = int(input(texto))
            break
        except:
            print("Dato no valido.....")
    
    return numero



listaPrincipal = []

def crear_lista():
    
    dato = validarNumero("Cuantos numeros desea agregar: ")
    
    contador = 0
    
    while contador < dato:
        numero = validarNumero(f'Ingrese numero {contador + 1}: ')
        listaPrincipal.append(numero)
        contador +=1
        
    
    print(f'La lista a cambiar es: {listaPrincipal}')
    
    return listaPrincipal


def reemplazar_numero(lista, numero):
    numero_dado = numero
    
    for i in range(len(lista)):
        
        if lista[i] == numero_dado:
            lista[i] = "*"
    
    for lis in lista:
        print(lis)
    
    
        


crear_lista()

numero_reemplar = validarNumero("Ingrese el numero a reemplazar: ")
reemplazar_numero(listaPrincipal, numero_reemplar)
