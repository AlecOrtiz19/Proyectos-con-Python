import peewee
import ValidacionesORM as validar


base_de_datos = peewee.MySQLDatabase('biblioteca', host= "localhost", port=3306, user="root", password="12345")

class User(peewee.Model):
    id_user = peewee.IntegerField()
    nombre = peewee.CharField()
    apellido = peewee.CharField()
    fecha_nacimiento = peewee.DateField()
    direccion = peewee.CharField()
    
    class Meta:
        
        database = base_de_datos
        table_name = 'usuarios'


    def consultar_usuarios(usuario, dato_buscar):
        
        usuarios = User.select().where(User.nombre == dato_buscar)
        
        if validar.validar_existencia(User, dato_buscar):
            for usuario in usuarios:
                print(f'Nombre: {usuario.nombre} \n Apellido: {usuario.apellido} \n Fecha nacimiento: {usuario.fecha_nacimiento} \n Direccion: {usuario.direccion} ')
        else:
            print("El usuario no existe...")
            
    def eliminar_usuario(usuario, dato_borrar):
        
        if validar.validar_existencia(User, dato_borrar):
            
            query = User.delete().where(User.nombre == dato_borrar)
            query.execute()
            print("El usuario fue eliminado...")
        else:
            print("El usuario que se desea elminar no existe...")
            
    def actualizar_usuario(usuario, dato_actualizar, dato_nuevo):
        
        if validar.validar_existencia(User, dato_actualizar):
            query = User.update(nombre = dato_nuevo).where(usuario.nombre == dato_actualizar)
            query.execute()
            print("Usuario Actualizado con exito")
        else:
            print("El dato que desea actualizar no existe")
        
def validar_opcion(text):
    while True:
        try:
            opcion = int(input(text))
            break
        except:
            print("Solo numeros...")
    return opcion

def menu():
    
    print("1. REGISTRAR \n 2. COSULTAR \n 3. ELIMINAR \n 4. ACTUALIZAR \n 5. TERMINAR")
        
if __name__ == "__main__":
    clase = User
    
    
    while True:
    
        menu()
    
        opcion = validar_opcion("Escoja una opcion entre 1 y 2: ")
    
        if opcion == 1:
        
            if not User.table_exists():
                base_de_datos.connect()
                base_de_datos.create_tables([User])
            
            username = input("Ingrese un nombre: ")
            apellido = input("Ingrese un apellido: ")
            nacimiento = input("Ingrese la fecha de nacimiento: ")
            direccion = input("Ingrese la direccion: ")
                
                
            if not User.select().where(User.nombre == username).exists():
                nuevo_usuario = User.create(nombre=username, apellido=apellido, fecha_nacimiento=nacimiento, direccion=direccion)
                nuevo_usuario.save()
                
            else:
                print("El usuario ya existe...")
        elif opcion == 2:
            
            nombre_a_buscar = input("Ingrese el nombre a buscar: ")
            
            clase.consultar_usuarios(User, nombre_a_buscar)

        elif opcion == 3:
            
            nombre_a_eliminar = input("Ingrese el nombre a eliminar: ")
            
            clase.eliminar_usuario(User, nombre_a_eliminar)

        elif opcion == 4:
            
            dato_actualizar = input("Ingrese el nombre que desea actualizar: ")
            
            nuevo_dato = input("Ingrese el nuevo valor: ")
            
            clase.actualizar_usuario(User, dato_actualizar, nuevo_dato)
            
        elif opcion == 5:
            print("Terminado")
            break