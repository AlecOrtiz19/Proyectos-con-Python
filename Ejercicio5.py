class Pila:
    def __init__(self):
        self.caracteres = []

    def esta_vacia(self):
        return self.caracteres == []

    def apilar(self, item):
        self.caracteres.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.caracteres.pop()

    def ver_tope(self):
        if not self.esta_vacia():
            return self.caracteres[-1]
        
        
def mostrar_ascii(pila):
    print("Elementos ingresadoASCII:")
    while not pila.esta_vacia():
        elemento = pila.desapilar()
        codigo_ascii = ord(elemento)
        print(f"Caracter: {elemento} Su Codigo ASCII: {codigo_ascii}")



def ingresar_caracteres():
    pila_caracteres = Pila()

    while True:
        caracter = input("Ingrese un carácter (* para finalizar): ")
        
        if caracter == "*":
            mostrar_ascii(pila_caracteres)
            break
        else:
            pila_caracteres.apilar(caracter)



ingresar_caracteres()
